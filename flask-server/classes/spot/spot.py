from classes.spot.spot_connection import SpotConnection
from classes.spot.spot_controller import SpotController
from classes.spot.spot_video_streamer import SpotVideoStreamer
from classes.spot.spot_audio_streamer import SpotAudioStreamer



class Spot:
    spot_connection: SpotConnection = spot_connection
    spot_controller: SpotController = spot_controller
    video_streamer: SpotVideoStreamer = video_streamer
    audio_streamer: SpotAudioStreamer = audio_streamer


    def __init__(self, spot_connection: SpotConnection = None, spot_controller: SpotController = None, video_streamer:SpotVideoStreamer = None, audio_streamer: SpotAudioStreamer = None):
        self.spot_connection: SpotConnection = spot_connection
        self.spot_controller: SpotController = spot_controller
        self.video_streamer: SpotVideoStreamer = video_streamer
        self.audio_streamer: SpotAudioStreamer = audio_streamer

        pass
