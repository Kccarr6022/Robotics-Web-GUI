from pythonping import ping
import bosdyn.client

class SpotConnection:
    host: str
    sdk = None
    robot = None

    def __init__(self, host:str= None):
        self.host = host
        print('connecting...')
        if self.is_there():
            try:
                self.sdk = bosdyn.client.create_standard_sdk('fermi-spot')
                # Initialize a Robot Object
                self.robot = self.sdk.create_robot(host)
                print(f'Connection established to spot on address: {host}')
            except Exception as e:
                print(f"Successful ping on address: {host}, could not connect", e)
        else:
            print(f"Unsuccessful ping on address: {host}")


    def is_there(self):
        # ping fermi-spot to see if it connected to the network
        ping_result = ping('192.168.80.3', count=1)
        # Option = 1 - SuccessOn.One, 2 - SuccessOn.Most, 3 - SuccessOn.All
        return True if ping_result.success(option=3) else False

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