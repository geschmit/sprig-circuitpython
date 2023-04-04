from sprig_circuitpython import Sprig
from array import array
from math import sin, pi
from audiocore import RawSample

# adjust these, as needed
tone_volume = 0.05
frequency = 440
length = 8000

sine_wave = array("h", [0] * length)
for i in range(length):
    sine_wave[i] = int((sin(pi * 2 * i / length)) * tone_volume * (2 ** 15 - 1))

sine_wave_sample = RawSample(sine_wave)
sprig = Sprig()

sprig.speaker.play(sine_wave_sample)
sprig.poll_input()
sprig.speaker.stop()