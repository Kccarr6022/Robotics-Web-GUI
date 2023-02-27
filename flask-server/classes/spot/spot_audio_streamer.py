from classes.spot.spot_connection import SpotConnection

class SpotAudioStreamer:
    spot_connection: SpotConnection

    def __init__(self, spot_connection: SpotConnection):
        self.spot_connection: SpotConnection = spot_connection
