from pythonping import ping
import bosdyn.client

class SpotConnection:
    host: str
    sdk = None
    robot = None

    def __init__(self, host:str, username: str, password: str):
        self.host = host
        print('connecting...')
        if self.is_there():
            try:
                self.sdk = bosdyn.client.create_standard_sdk('fermi-spot')
                # Initialize a Robot Object
                self.robot = self.sdk.create_robot(host)
                print(f'Connection established to spot on address: {host}')
                self.authenticate(username=username, password=password)
            except Exception as e:
                print(f"Successful ping on address: {host}, could not connect", e)
        else:
            print(f"Unsuccessful ping on address: {host}")

    def authenticate(self, username: str, password: str):
        if self.is_on(self.robot):
            # ask Fermilab what the robot username and password are
            # or make them enter in the username and password when they make the robotic systems selection
            self.robot.authenticate(username, password)

    def reconnect(self):
        print('reconnecting...')
        if self.is_there():
            try:
                self.sdk = bosdyn.client.create_standard_sdk('fermi-spot')
                # Initialize a Robot Object
                self.robot = self.sdk.create_robot(self.host)
                print(f'Connection established to spot on address: {self.host}')
            except Exception as e:
                print(f"Successful ping on address: {self.host}, could not connect", e)
        else:
            print(f"Unsuccessful ping on address: {self.host}")

    def is_on(self):
        if self.robot.is_powered_on():
            print('Spot is online')
            return True
        else:
            print('Spot is powered off')
            return False

    def is_there(self):
        # ping fermi-spot to see if it connected to the network
        ping_result = ping('192.168.80.3', count=1)
        # Option = 1 - SuccessOn.One, 2 - SuccessOn.Most, 3 - SuccessOn.All
        return True if ping_result.success(option=3) else False