from classes.spot.spot_connection import SpotConnection

class SpotVideoStreamer:
    spot_connection: SpotConnection

    def __init__(self, spot_connection: SpotConnection = None):
        self.spot_connection: SpotConnection = spot_connection

    pass