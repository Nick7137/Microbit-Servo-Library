from microbit import *   # this is necessary for the servo class to work

from servo import Servo  # imports class "Servo" from module "servo.py"

LIMIT_ARROW_W = Image(  # creates image to display when angle excedes 180°
             "90900:"
             "99000:"
             "99999:"
             "99000:"
             "90900")

LIMIT_ARROW_E = Image(  # creates image to display when angle dips below 0°
             "00909:"
             "00099:"
             "99999:"
             "00099:"
             "00909")

angle = 0
delta_angle = 90   # defines how much servo increments with each button press

servo1 = Servo(pin13)   # creates servo object and defines output on pin15, almost every pin will work
servo1.rotate(angle)    # rotates servo1 to angle degrees on startup

while True:
    if button_a.get_presses() == 1:
        display.show(Image.ARROW_W)
        angle = angle + delta_angle   # angle increments
        if angle >= 180:   # prevents exception being raised from servo library as servo cannot rotate more than 180°
            angle = 180
            display.show(LIMIT_ARROW_W) # shows limit arrow designed earlier
        servo1.rotate(angle)  # executes rotation

    if button_b.get_presses() == 1:
        display.show(Image.ARROW_E)
        angle = angle - delta_angle
        if angle <= 0:
            angle = 0
            display.show(LIMIT_ARROW_E)
        servo1.rotate(angle)