import RPi.GPIO as GPIO
import time


class RaspLight:

    def __init__(self) -> None:
        super().__init__()
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
                GPIO.output(self.PIN_22, True)
                GPIO.output(self.PIN_19, True)
                print("Red1 is on")
                time.sleep(3)
                GPIO.output(self.PIN_19, False)
                print("red1 is off")
                GPIO.output(self.PIN_20, True)
                print("yellow1 is on")
                time.sleep(1)
                GPIO.output(self.PIN_20, False)
                print("yellow1 is off")
                GPIO.output(self.PIN_21, True)
                print("green1 is on")
                time.sleep(5)
                GPIO.output(self.PIN_21, False)
                print("green1 is off")
                GPIO.output(self.PIN_20, True)
                print("yellow1 is on")
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
                print("Green 2 is on")
                time.sleep(5)
                print("After sleep")
                GPIO.output(self.PIN_24, False)

                time.sleep(1)
                GPIO.output(self.PIN_23, True)
                time.sleep(1)
                GPIO.output(self.PIN_23, False)
                GPIO.output(self.PIN_22, True)
        except KeyboardInterrupt as ki:
            GPIO.cleanup()
            print("You  have exited successfully", ki)