
#define TV class
# Define TV class , channel and volume
class TV:
    def __init__(self, channel=1, volume=1):
        self._channel = channel
        self._volume = volume
        self._is_on = False

    def turn_on(self):
        self._is_on = True

    def turn_off(self):
        self._is_on = False

    def get_channel(self):
        return self._channel

    def set_channel(self, channel):
        if 1 <= channel <= 30:
            self._channel = channel
        else:
            raise ValueError("Channel must be between 1 and 30")

    def get_volume(self):
        return self._volume

    def set_volume(self, volume):
        if 1 <= volume <= 100:
            self._volume = volume
        else:
            raise ValueError("Volume must be between 1 and 100")

    def channel_up(self):
        if self._channel < 30:
            self._channel += 1

    def channel_down(self):
        if self._channel > 1:
            self._channel -= 1

    def volume_up(self):
        if self._volume < 100:
            self._volume += 1

    def volume_down(self):
        if self._volume > 1:
            self._volume -= 1

# Define TestTV class
class TestTV:
    def __init__(self):
        self.tv1 = TV()
        self.tv2 = TV()

#user input channel and volume 
    def run_test(self):
        # Input for TV1
        channel1 = int(input("Enter channel for TV1 (1-30): "))
        volume1 = int(input("Enter volume for TV1 (1-100): "))
        self.tv1.set_channel(channel1)
        self.tv1.set_volume(volume1)

        # Input for TV2
        channel2 = int(input("Enter channel for TV2 (1-30): "))
        volume2 = int(input("Enter volume for TV2 (1-100): "))
        self.tv2.set_channel(channel2)
        self.tv2.set_volume(volume2)

        # Output the channel and volume for both TVs
        print(f"TV1's channel is {self.tv1.get_channel()} and volume level is {self.tv1.get_volume()}")
        print(f"TV2's channel is {self.tv2.get_channel()} and volume level is {self.tv2.get_volume()}")

# Create an instance of TestTV and run the test
test = TestTV()
test.run_test()
