import RPi.GPIO as GPIO
import time

class RaspLight:

    def __init__(self) -> None:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.PIN_19 = 19
        self.PIN_20 = 20
        self.PIN_21 = 21
        self.PIN_22 = 22
        self.PIN_23 = 23
        self.PIN_24 = 24
        GPIO.setup(self.PIN_19, GPIO.OUT)  # red1
        GPIO.setup(self.PIN_20, GPIO.OUT)  # yellow1
        GPIO.setup(self.PIN_21, GPIO.OUT)  # green1
        GPIO.setup(self.PIN_22, GPIO.OUT)  # red2
        GPIO.setup(self.PIN_23, GPIO.OUT)  # yellow2
        GPIO.setup(self.PIN_24, GPIO.OUT)  # green2

    def control_lights(self):
        try:
            while True:
                GPIO.output(self.PIN_19, True)
                GPIO.output(self.PIN_22, True)
                time.sleep(3)
                GPIO.output(self.PIN_19, False)
                GPIO.output(self.PIN_20, True)
                time.sleep(1)
                GPIO.output(self.PIN_20, False)
                GPIO.output(self.PIN_21, True)
                time.sleep(5)
                GPIO.output(self.PIN_21, False)
                GPIO.output(self.PIN_20, True)
                time.sleep(2)
                GPIO.output(self.PIN_20, False)
                GPIO.output(self.PIN_19, True)
                GPIO.output(self.PIN_19, False)
                GPIO.output(self.PIN_19, True)
                GPIO.output(self.PIN_22, False)
                GPIO.output(self.PIN_23, True)
                time.sleep(1)
                GPIO.output(self.PIN_23, False)
                GPIO.output(self.PIN_24, True)
                time.sleep(5)
                GPIO.output(self.PIN_24, False)
                GPIO.output(self.PIN_23, True)
                time.sleep(1)
                GPIO.output(self.PIN_23, False)
        except KeyboardInterrupt as ki:
            GPIO.cleanup()
            print("You  have exited successfully", ki)