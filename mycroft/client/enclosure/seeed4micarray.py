"""
Enclosure for PiCroft with a 4MicArray by Seeed
"""

import time

# Number of LEDs on the Seed 4 Mic Hat
NUMBER_OF_LEDS = 12


def event_access_handled(method):
    """
    Call method with event and handle typical access errors
    """
    def handled_method(self, event):
        try:
            self.method(event)
        except (AttributeError, KeyError, IndexError):
            # Invalid event object passed
            pass
    return handled_method


class Enclosure4MicArray:
    """
    This Enclosure is meant to implement responsive MyCroft on a PiCroft
    with an installed Seeed 4 Mic array. The LEDs on the Array are to be used.
    """

    def __init__(self, ws):
        self.ws = ws
        self.__init_events()

    def __init_events(self):
        self.ws.on('enclosure.mouth.reset', self.mouth_reset)
        self.ws.on('enclosure.mouth.talk', self.mouth_talk)
        self.ws.on('enclosure.mouth.think', self.mouth_think)
        self.ws.on('enclosure.mouth.listen', self.mouth_listen)
        self.ws.on('enclosure.mouth.smile', self.mouth_smile)
        self.ws.on('enclosure.mouth.viseme', self.mouth_viseme)
        self.ws.on('enclosure.system.reset', self.reset)
        self.ws.on('enclosure.system.blink', self.system_blink)
        self.ws.on('enclosure.eyes.on', self.eyes_on)
        self.ws.on('enclosure.eyes.off', self.eyes_off)
        self.ws.on('enclosure.eyes.blink', self.eyes_blink)
        self.ws.on('enclosure.eyes.narrow', self.eyes_narrow)
        self.ws.on('enclosure.eyes.look', self.eyes_look)
        self.ws.on('enclosure.eyes.color', self.eyes_color)
        self.ws.on('enclosure.eyes.level', self.eyes_brightness)
        self.ws.on('enclosure.eyes.volume', self.eyes_volume)
        self.ws.on('enclosure.eyes.spin', self.eyes_spin)
        self.ws.on('enclosure.eyes.timedspin', self.eyes_timed_spin)
        self.ws.on('enclosure.eyes.reset', self.eyes_reset)
        self.ws.on('enclosure.eyes.setpixel', self.eyes_setpixel)
        self.ws.on('enclosure.eyes.fill', self.eyes_fill)

    def reset(self, event=None):
        """The enclosure should restore itself to a started state.
        Implemented by turning off all LEDs
        """
        # TODO turn off
        pass

    @event_access_handled
    def system_blink(self, event=None):
        """The 'eyes' should blink the given number of times.
        Implemented by blinking LEDs in default colors
        As a system call, this should blink slower than eye/talk blink
        Event-Args:
            times (int): number of times to blink
        """
        n = event.data['times']
        # TODO blink n times

    def eyes_on(self, event=None):
        """Illuminate or show the eyes.
        Implemented by turning on LEDs in default colors"""
        # TODO turn on LEDs
        pass

    def eyes_off(self):
        """Turn off or hide the eyes."""
        self.reset()

    def eyes_blink(self, event=None):
        """Make the eyes blink once
        Blink all LEDs, slow
        Event-Args:
            side (str): 'r', 'l', or 'b' for 'right', 'left' or 'both'
        """
        # ignore side
        # TODO blink all LEDs once
        pass

    def eyes_narrow(self):
        """Make the eyes look narrow, like a squint"""
        # TODO turn off LEDs towards the middle on both sides
        pass

    @event_access_handled
    def eyes_look(self, event):
        """Make the eyes look to the given side
        Event-Args:
            side (str): 'r' for right
                        'l' for left
                        'u' for up
                        'd' for down
                        'c' for crossed
        """
        # TODO let all LEDs collect on one side => only one LED remaining on that side
        pass

    @event_access_handled
    def eyes_color(self, event):
        """Change the eye color to the given RGB color
        Event-Args:
            r (int): 0-255, red value
            g (int): 0-255, green value
            b (int): 0-255, blue value
        """
        # TODO colorize all LEDs in given color
        pass

    @event_access_handled
    def eyes_setpixel(self, event):
        """Set individual LEDs of the mic hat
        Event-Args:
            idx (int): number of desired LED
            r (int): The red value to apply
            g (int): The green value to apply
            b (int): The blue value to apply
        """
        # 4MicHat has exactly half as many LEDs as the mycroft
        # by modulu operation, the programmer is able to display exactly one eye on the hat
        idx = event.data['idx'] % NUMBER_OF_LEDS
        # TODO set LED with idx%amountofLEDs to given color

    @event_access_handled
    def eyes_fill(self, event):
        """Use the LEDs as a type of progress meter
        Event-Args:
            percentage (int):
        """
        percentage = event.data['percentage']
        if percentage < 0 or percentage > 100:
            raise ValueError('percentage ({}) must be between 0-100'.
                             format(str(percentage)))
        n = int((percentage * NUMBER_OF_LEDS)/100)
        # TODO colorize n LEDs

    @event_access_handled
    def eyes_brightness(self, event=None):
        """Set the brightness of the eyes in the display.
        Event-Args:
            level (int): 1-30, bigger numbers being brighter
        """
        # TODO check if possible on 4 Mic Hat
        pass

    def eyes_reset(self, event=None):
        """Restore the eyes to their default (ready) state."""
        self.eyes_on()

    def eyes_spin(self, event=None):
        """Make one LED spin once
        """
        # TODO make the LEDs spin
        pass

    @event_access_handled
    def eyes_timed_spin(self, event=None):
        """Make the LEDs spin for the given time.
        Event-Args:
            length (int): duration in milliseconds of roll, None = forever
        """
        # TODO spin
        pass

    @event_access_handled
    def eyes_volume(self, event):
        """Indicate the volume using the eyes
        Event-Args:
            volume (int): 0 to 11
        """
        volume = event.data['volume']
        if volume < 0 or volume > 11:
            raise ValueError('volume ({}) must be between 0-11'.
                             format(str(volume)))
        n = volume+1
        # TODO colorize n LEDs (12 leds for 12 volume steps, ka-ching)

    def mouth_reset(self, event=None):
        """Restore the mouth display to normal (blank)
        Turns off LEDs"""
        self.reset()

    def mouth_talk(self, event=None):
        """Show a generic 'talking' animation for non-synched speech
        Implemented by blinking LEDs"""
        # TODO feature: extracting direction of speak and looking there
        # TODO blink LEDs in a fix, natural looking time span
        # like short short long short long long long
        pass

    def mouth_think(self, event=None):
        """Show a 'thinking' image or animation
        Implemented by spinning LEDs, similar to loading image"""
        # TODO loading spin
        pass

    def mouth_listen(self, event=None):
        """Show a 'thinking' image or animation
        Implemented by glowing"""
        self.eyes_on()

    def mouth_smile(self, event=None):
        """Show a 'smile' image or animation
        Implemented by one round of spinning, then only LEDs on"""
        self.eyes_spin()
        self.eyes_on()

    def mouth_viseme(self, event=None):
        """Display a viseme mouth shape for synched speech
        Not implemented, same as mouth_talk
        Event-Args:
            code (int):  0 = shape for sounds like 'y' or 'aa'
                         1 = shape for sounds like 'aw'
                         2 = shape for sounds like 'uh' or 'r'
                         3 = shape for sounds like 'th' or 'sh'
                         4 = neutral shape for no sound
                         5 = shape for sounds like 'f' or 'v'
                         6 = shape for sounds like 'oy' or 'ao'
            time_until (float): (optional) For timing, time.time() when this
                         shape expires, or 0 for display regardles of time
        """
        time_until = event.data.get('time_until')
        # skip if no deadline or deadline not violated
        if not time_until or time.time() < time_until:
            self.mouth_talk()

