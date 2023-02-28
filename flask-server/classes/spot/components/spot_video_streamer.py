from spot_connection import SpotConnection
import logging
import argparse
import sys
import cv2
import numpy as np
from scipy import ndimage
from flask import Response, Flask, render_template

from bosdyn.api import image_pb2
import bosdyn.client
from bosdyn.client.time_sync import TimedOutError
import bosdyn.client.util
from bosdyn.client.image import ImageClient, build_image_request

_LOGGER = logging.getLogger(__name__)

ROTATION_ANGLE = {
    'back_fisheye_image': 0,
    'frontleft_fisheye_image': -78,
    'frontright_fisheye_image': -102,
    'left_fisheye_image': 0,
    'right_fisheye_image': 180
}


class SpotVideoStreamer:
    spot_connection: SpotConnection

    def __init__(self, spot_connection: SpotConnection = None):
        self.spot_connection: SpotConnection = spot_connection

    def image_to_opencv(self, image, auto_rotate=True):
        """Convert an image proto message to an openCV image"""
        num_channels = 1  # Assume a default of 1 byte encodings.
        if image.shot.image.pixel_format == image_pb2.Image.PIXEL_FORMAT_DEPTH_U16:
            dtype = np.uint16
            extension = ".png"
        else:
            dtype = np.uint8
            if image.shot.image.pixel_format == image_pb2.Image.PIXEL_FORMAT_RGB_U8:
                num_channels = 3
            elif image.shot.image.pixel_format == image_pb2.Image.PIXEL_FORMAT_RGBA_U8:
                num_channels = 4
            elif image.shot.image.pixel_format == image_pb2.Image.PIXEL_FORMAT_GREYSCALE_U8:
                num_channels = 1
            elif image.shot.image.pixel_format == image_pb2.Image.PIXEL_FORMAT_GREYSCALE_U16:
                num_channels = 1
                dtype = np.uint16
            extension = ".jpg"

        img = np.frombuffer(image.shot.image.data, dtype=dtype)
        if image.shot.image.format == image_pb2.Image.FORMAT_RAW:
            try:
                # Attempt to reshape array into a RGB rows X cols shape.
                img = img.reshape((image.shot.image.rows, image.shot.image.cols, num_channels))
            except ValueError:
                # Unable to reshape the image data, trying a regular decode.
                img = cv2.imdecode(img, -1)
        else:
            img = cv2.imdecode(img, -1)

        if auto_rotate:
            img = ndimage.rotate(img, ROTATION_ANGLE[image.source.name])

        return img, extension

    def reset_image_client(self):
        """Recreate the ImageClient from the robot object"""
        del self.spot_connection.robot.service_clients_by_name['image']
        del self.spot_connection.robot.channels_by_authority['api.spot.robot']
        return self.spot_connection.robot.ensure_client('image')

    def generate(self):
        """Generate image from robot"""
        value_for_q_keystroke = 113
        value_for_esc_keystroke = 27

        # Parse args
        args = sys.argv[1:]
        parser = argparse.ArgumentParser()
        bosdyn.client.util.add_base_arguments(parser)
        parser.add_argument('--image-sources', help='Get image from source(s)', action='append')
        parser.add_argument('--image-service', help='Name of the image service to query.',
                        default=ImageClient.default_service_name)
        parser.add_argument('-j', '--jpeg-quality-percent', help="JPEG quality percentage (0-100)",
                        type=int, default=50)
        parser.add_argument('-c', '--capture-delay', help="Time [ms] to wait before the next capture",
                        type=int, default=100)
        parser.add_argument('--disable-full-screen',
                        help="Default display is full screen. This flag disables that.",
                        action='store_true')
        parser.add_argument('--auto-rotate', help='rotate right and front images to be upright',
                        action='store_true')
        parser.add_argument("-i", "--ip", type=str,
                        help="ip address of the device")
        parser.add_argument("-o", "--port", type=int,
                        help="ephemeral port number of the server (1024 to 65535)")
        options = parser.parse_args(args)

        self.spot_connection.robot.sync_with_directory()
        self.spot_connection.robot.time_sync.wait_for_sync()

        image_client = self.spot_connection.robot.ensure_client(options.image_service)
        requests = [
            build_image_request(source, quality_percent=options.jpeg_quality_percent)
            for source in options.image_sources
        ]

        keystroke = None
        timeout_count_before_reset = 0
        while keystroke != value_for_q_keystroke and keystroke != value_for_esc_keystroke:
            try:
                images_future = image_client.get_image_async(requests, timeout=0.5)
                while not images_future.done():
                    keystroke = cv2.waitKey(25)
                    print(keystroke)
                    if keystroke == value_for_esc_keystroke or keystroke == value_for_q_keystroke:
                        sys.exit(1)
                images = images_future.result()
            except TimedOutError as time_err:
                if timeout_count_before_reset == 5:
                    # To attempt to handle bad comms and continue the live image stream,
                    # try recreating the image client after having an RPC timeout 5 times.
                    _LOGGER.info("Resetting image client after 5+ timeout errors.")
                    image_client = self.reset_image_client(self.spot_connection.robot)
                    timeout_count_before_reset = 0
                else:
                    timeout_count_before_reset += 1
            except Exception as err:
                _LOGGER.warning(err)
                continue
            for i in range(len(images)):
                image, _ = self.image_to_opencv(images[i], options.auto_rotate)
                _, image = cv2.imencode('.jpg', image)
                image = image.tobytes()
            yield b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n'
            keystroke = cv2.waitKey(options.capture_delay)