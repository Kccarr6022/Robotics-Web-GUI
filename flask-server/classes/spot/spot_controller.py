from classes.spot.spot_connection import SpotConnection

class SpotController:
    spot_connection: SpotConnection

    def __init__(self, spot_connection: SpotConnection = None):
        self.spot_connection = spot_connection

    pass