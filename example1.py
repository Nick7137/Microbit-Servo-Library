from microbit import *   # this is necessary for the servo class to work

class Servo:

    PWM_period = 20 # defines PWM period in ms - for Tower Pro SG90, PWM period = 20ms

    # allows control of a servo motor from any available pin on the micro:bit
    # The voltage to power the servo must be 5V. The signal voltage ideally should also be 5V
    # but the servo will work with the 3.3V that the micro:bit provides. A two transistor
    # amplifier circuit can be used to achieve a 5V signal.

    def __init__(self, pin):
        self.my_pin = pin
        self.my_pin.set_analog_period(self.PWM_period) #sets analogue period to PWM_period ms

    def rotate(self, new_angle):
        if new_angle > 180:
            # micro:bit automatically displays exception to user
            raise Exception("angle > 180 degrees") #servo cannot rotate more than 180°
        elif new_angle < 0:
            raise Exception("angle < 0 degrees") #servo cannot rotate less than 0°
        else:
            # Calculating analogue input:
            # First calculate duty cycle needed for the given angle input.
            # Datasheet says for Tower Pro SG90 pulse_width_range is 1000us to 2000us.
            # From measurements, actual pulse_width_range is 500us to 2500us.
            # Define duty_cycle_ratio = pulse_width/PWM_period
            # angle:                   0°      90°     180°        and everything inbetween
            # pulse_width:             500us   1500us  2500us
            # duty_cycle_ratio:        1/40    3/40    5/40
            # therefore formula for converting angle to duty_cycle_ratio is:
            # = 1/40 + angle*(duty_cycle_ratio range/angle range
            # = 1/40 + angle*(5/40 - 1/40)/(180 - 0)
            # = 1/40 + angle/1800
            # Calculating analogue_input from duty_cycle_ratio.
            # duty_cycle_ratio:        0       1/40     5/40    1
            # analogue_input:          0       25.6     128     1024
            # multiplier is x1024
            # Note: if constant voltage is desired, analogue input of 1024 returns an error,
            #       instead, a digital signal may be used.
            analogue_input = (1/40 + new_angle/1800)*1024
            self.my_pin.write_analog(analogue_input)

# end of library


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