# include GPIO and Timer Library
import RPi.GPIO as GPIO
import time


class led57_object(object):
    def __init__(self):
        # define Raspberry Pi GPIO number
        self.sleeptime = 0.001
        self.COL1 = 7
        self.COL2 = 11
        self.COL3 = 13
        self.COL4 = 15
        self.COL5 = 29
        self.COL6 = 31
        self.COL7 = 33
        self.COL8 = 35
        self.ROW1 = 12
        self.ROW2 = 16
        self.ROW3 = 18
        self.ROW4 = 22
        self.ROW5 = 32
        self.ROW6 = 36
        self.ROW7 = 38
        self.ROW8 = 40
        self.ROWS = [self.ROW1, self.ROW2, self.ROW3, self.ROW4, self.ROW5, self.ROW6, self.ROW7, self.ROW8]
        self.COLS = [self.COL1, self.COL2, self.COL3, self.COL4, self.COL5, self.COL6, self.COL7, self.COL8]

        # Raspberry Pi GPIO initalization
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.COL1, GPIO.OUT)
        GPIO.setup(self.COL2, GPIO.OUT)
        GPIO.setup(self.COL3, GPIO.OUT)
        GPIO.setup(self.COL4, GPIO.OUT)
        GPIO.setup(self.COL5, GPIO.OUT)
        GPIO.setup(self.COL6, GPIO.OUT)
        GPIO.setup(self.COL7, GPIO.OUT)
        GPIO.setup(self.COL8, GPIO.OUT)
        GPIO.setup(self.ROW1, GPIO.OUT)
        GPIO.setup(self.ROW2, GPIO.OUT)
        GPIO.setup(self.ROW3, GPIO.OUT)
        GPIO.setup(self.ROW4, GPIO.OUT)
        GPIO.setup(self.ROW5, GPIO.OUT)
        GPIO.setup(self.ROW6, GPIO.OUT)
        GPIO.setup(self.ROW7, GPIO.OUT)
        GPIO.setup(self.ROW8, GPIO.OUT)

    def clear(self):
        # set all GPIO output to LOW
        GPIO.output(self.COL1, GPIO.LOW)
        GPIO.output(self.COL2, GPIO.LOW)
        GPIO.output(self.COL3, GPIO.LOW)
        GPIO.output(self.COL4, GPIO.LOW)
        GPIO.output(self.COL5, GPIO.LOW)
        GPIO.output(self.COL6, GPIO.LOW)
        GPIO.output(self.COL7, GPIO.LOW)
        GPIO.output(self.COL8, GPIO.LOW)
        GPIO.output(self.ROW1, GPIO.LOW)
        GPIO.output(self.ROW2, GPIO.LOW)
        GPIO.output(self.ROW3, GPIO.LOW)
        GPIO.output(self.ROW4, GPIO.LOW)
        GPIO.output(self.ROW5, GPIO.LOW)
        GPIO.output(self.ROW6, GPIO.LOW)
        GPIO.output(self.ROW7, GPIO.LOW)
        GPIO.output(self.ROW8, GPIO.LOW)

    def drawRow(self, row_string, row_index):
        self.clear()
        GPIO.output(self.ROWS[row_index], GPIO.HIGH)
        for bit in range(0, 8):
            GPIO.output(self.COLS[bit], GPIO.HIGH if row_string[bit] == "1" else GPIO.LOW)
        time.sleep(self.sleeptime)

    def drawMatrix(self, matrix):
        for bit in range(0, 8):
            self.drawRow(matrix[bit], bit)

    def demo(self):
        # Code sample of showing 'Pi'
        while 1:

            matrix = [
                "10101101",
                "00101101",
                "00001101",
                "00001100",
                "00101100",
                "00101100",
                "10101000",
                "10000000",
            ]
            self.drawMatrix(matrix)

            # self.clear()
            # GPIO.output(self.ROW1, GPIO.HIGH)
            # GPIO.output(self.COL1, GPIO.LOW)
            # GPIO.output(self.COL2, GPIO.LOW)
            # GPIO.output(self.COL3, GPIO.LOW)
            # GPIO.output(self.COL4, GPIO.HIGH)
            # GPIO.output(self.COL5, GPIO.HIGH)
            # GPIO.output(self.COL6, GPIO.LOW)
            # GPIO.output(self.COL7, GPIO.HIGH)
            # time.sleep(self.sleeptime)

            # self.clear()
            # GPIO.output(self.ROW2, GPIO.HIGH)
            # GPIO.output(self.COL1, GPIO.LOW)
            # GPIO.output(self.COL2, GPIO.HIGH)
            # GPIO.output(self.COL3, GPIO.HIGH)
            # GPIO.output(self.COL4, GPIO.LOW)
            # GPIO.output(self.COL5, GPIO.HIGH)
            # GPIO.output(self.COL6, GPIO.HIGH)
            # GPIO.output(self.COL7, GPIO.HIGH)
            # time.sleep(self.sleeptime)

            # self.clear()
            # GPIO.output(self.ROW3, GPIO.HIGH)
            # GPIO.output(self.COL1, GPIO.LOW)
            # GPIO.output(self.COL2, GPIO.LOW)
            # GPIO.output(self.COL3, GPIO.LOW)
            # GPIO.output(self.COL4, GPIO.HIGH)
            # GPIO.output(self.COL5, GPIO.HIGH)
            # GPIO.output(self.COL6, GPIO.LOW)
            # GPIO.output(self.COL7, GPIO.HIGH)
            # time.sleep(self.sleeptime)

            # self.clear()
            # GPIO.output(self.ROW4, GPIO.HIGH)
            # GPIO.output(self.COL1, GPIO.LOW)
            # GPIO.output(self.COL2, GPIO.HIGH)
            # GPIO.output(self.COL3, GPIO.HIGH)
            # GPIO.output(self.COL4, GPIO.HIGH)
            # GPIO.output(self.COL5, GPIO.HIGH)
            # GPIO.output(self.COL6, GPIO.LOW)
            # GPIO.output(self.COL7, GPIO.HIGH)
            # time.sleep(self.sleeptime)

            # self.clear()
            # GPIO.output(self.ROW5, GPIO.HIGH)
            # GPIO.output(self.COL1, GPIO.LOW)
            # GPIO.output(self.COL2, GPIO.HIGH)
            # GPIO.output(self.COL3, GPIO.HIGH)
            # GPIO.output(self.COL4, GPIO.HIGH)
            # GPIO.output(self.COL5, GPIO.HIGH)
            # GPIO.output(self.COL6, GPIO.LOW)
            # GPIO.output(self.COL7, GPIO.HIGH)
            # time.sleep(self.sleeptime)


def main():
    ledobj = led57_object()
    ledobj.demo()


if __name__ == "__main__":
    main()
