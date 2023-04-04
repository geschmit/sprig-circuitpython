# sprig-circuitpython
CircuitPython library to interface with the Sprig portable console, a hackable handheld running on a Raspberry Pi Pico.

# Installation
Ensure you have the latest version of CircuitPython installed. Tested with 8.X successfully.
This requires the `st7735r` library; please ensure you have it installed beforehand.

### Via pip
```
TODO
```

### Via Github
- Download a release from the releases tab, and clone it onto your Sprig's `/lib/` directory.

# Examples
All examples are located in the `examples/` directory.
```py
from sprig_circuitpython import Sprig
from time import sleep

sprig = Sprig()
sprig.ledLeft.value = True

while True:
    print("Hello, Sprig!")
    sprig.ledRight.value = not sprig.ledLeft.value
    sprig.ledLeft.value = not sprig.ledLeft.value
    sleep(0.25)
```

# Licensing
This project is licensed under GNU GPL v3.0.
"Sprig", the Sprig console and design are property of Hack Club.