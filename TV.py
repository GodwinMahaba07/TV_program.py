
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

#define TV test class
#input channel
#input volume 
#output channel and volume
