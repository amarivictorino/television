class TV:

    def __init__(self):
        self.channel = 1  
        self.volume_level = 1  
        self.on = False 

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        if 1 <= channel <= 120:
            self.channel = channel

    def get_volume(self):
        return self.volume_level

    def set_volume(self, volume_level):
        if 1 <= volume_level <= 7:
            self.volume_level = volume_level

    def channel_up(self):
        if self.on and self.channel < 120:
            self.channel += 1

    def channel_down(self):
        if self.on and self.channel > 1:
            self.channel -= 1

    def volume_up(self):
        if self.on and self.volume_level < 7:
            self.volume_level += 1

    def volume_down(self):  
        if self.on and self.volume_level > 1:
            self.volume_level -= 1

def main():
    tv1 = TV()
    tv2 = TV()

    tv1.turn_on()
    tv2.turn_on()

    tv1.set_channel(30)
    tv1.set_volume(3)
    tv2.set_channel(3)
    tv2.set_volume(2)

    print(f"tv1's channel is {tv1.get_channel()} and volume level is {tv1.get_volume()}")
    print(f"tv2's channel is {tv2.get_channel()} and volume level is {tv2.get_volume()}")

if __name__ == "__main__":
    main()


