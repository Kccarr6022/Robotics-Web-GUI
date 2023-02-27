from classes.spot.spot_connection import SpotConnection
from classes.spot.spot_controller import SpotController
from classes.spot.spot_video_streamer import SpotVideoStreamer
from classes.spot.spot_audio_streamer import SpotAudioStreamer
import bosdyn.client

class Spot:
    spot_connection: SpotConnection = spot_connection
    spot_controller: SpotController = spot_controller
    video_streamer: SpotVideoStreamer = video_streamer
    audio_streamer: SpotAudioStreamer = audio_streamer


    def __init__(self, host: str, username: str, password: str):
        self.spot_connection: SpotConnection = SpotConnection(host, username, password)
        self.spot_controller: SpotController = SpotController(spot_connection=self.spot_connection)
        self.video_streamer: SpotVideoStreamer = SpotVideoStreamer(spot_connection=self.spot_connection)
        self.audio_streamer: SpotAudioStreamer = SpotAudioStreamer(spot_connection=self.spot_connection)


    def power_on(self) -> bool:
        try:
            print('Spot powering on...')
            self.spot_connection.robot.power_on(timeout_sec=20)
        except bosdyn.client.power.PowerResponseError:
            print("Refer to Spot Documentation")
        except bosdyn.client.exceptions.RpcError:
            print("Refer to Spot Documentation")
        except bosdyn.client.power.CommandTimedOut:
            print("Refer to Spot Documentation")
        return self.spot_connection.is_on()