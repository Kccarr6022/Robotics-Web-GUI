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


    def __init__(self, spot_connection: SpotConnection = None, spot_controller: SpotController = None, video_streamer:SpotVideoStreamer = None, audio_streamer: SpotAudioStreamer = None):
        self.spot_connection: SpotConnection = spot_connection
        self.spot_controller: SpotController = spot_controller
        self.video_streamer: SpotVideoStreamer = video_streamer
        self.audio_streamer: SpotAudioStreamer = audio_streamer


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
        return self.status


    def status(self) -> bool:
        if self.spot_connection.robot.is_powered_on():
            print('Spot is online')
            return True
        else:
            print('Spot is powered off')
            return False

    def authenticate(self, username: str, password: str):
        if self.status(self.spot_connection.robot):
            # ask Fermilab what the robot username and password are
            # or make them enter in the username and password when they make the robotic systems selection
            self.spot_connection.robot.authenticate(username, password)