# Microbit-Servo-Library
## Intro:
This is a class which allows users to rotate hobby servos in Python using a micro:bit. It is specifically desinged for the Tower Pro SG90 servo motor but
will work with other servo motors such as the Tower Pro MG995, it could work on the Hextronic HXT900 but this has not been tested.
With regards to the SG90, some aspects of the datasheet are wrong and I developed this code from experimentation using an oscilloscope - this is commented in `servo.py`.\
The micro:bit can modulate the voltage on a pin thus allowing us to controll analogue devices such as servo motors, 
see: https://microbit-micropython.readthedocs.io/en/v1.0.1/pin.html. This means we don't need to use a time library which is unreliable as the internal clock may not accurate
enough for the small time intervals we are dealing with. Instead we can tell the micro:bit to set a pulse width modulation (PWM) period to a certain pin and then allow us to 
write analogue to that pin. The pins which can produce an analogue signal are: 0, 1, 2, 8, 12, 13, 14, 15 & 16, see link above for reference.
## How to use:
First you need to set up a circuit to control the servo. The voltage to **power the servo must be 5V**. The analogue signal voltage ideally should also have amplitude 5V, but the
micro:bit can only produce a 3.3V signal. This means a two transistor amplifier circuit can be used to achieve the 5V analogue signal. The good news is that the **Tower Pro SG90
will work with a 3.3V analogue signal** which means you can get away with connecting it straight to the micro:bit.\
There are two ways to use this class:
- The first is to copy the code of `servo.py` to the top of your programme, see `example1.py`. Flash the programme.
- The second is to import the module into your programme. The way this is done is by first copying `servo.py` to the `/mu_code/` directory of your PC. Then open the `Mu` application and press the `files` button. Connect your micro:bit to your PC. After a few seconds you will see `servo.py` under the `Files in your computer:` section. Drag `servo.py` into the `Files on your micro:bit:` section. Now you will be able to call the class. Flash `example2.py` and it should work.
#### Important notes:
The servo library only works if you import the micro:bit library at the top of your code. `from microbit import *`\
The syntax for importing the servo module is `from servo import Servo`, this imports class `Servo` from file `servo.py`
