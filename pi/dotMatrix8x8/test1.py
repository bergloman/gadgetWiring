# include GPIO and Timer Library
import RPi.GPIO as GPIO
import time


# pins1 = [7, 11, 13, 15, 29, 31, 33, 35]
# pins2 = [12, 16, 18, 22, 32, 36, 38, 40]
rows = [40, 18, 35, 32, 7, 33, 11, 29]
cols = [22, 13, 15, 38, 31, 36, 16, 12]


class led57_object(object):
    def __init__(self):
        # define Raspberry Pi GPIO number
        self.sleeptime = 0.001

        # collect all rows and columns for easier access
        self.ROWS = rows
        self.COLS = cols

        # Raspberry Pi GPIO initalization
        GPIO.setmode(GPIO.BOARD)
        for bit in range(0, 8):
            GPIO.setup(self.COLS[bit], GPIO.OUT)
            GPIO.setup(self.ROWS[bit], GPIO.OUT)

    def clear(self):
        for bit in range(0, 8):
            GPIO.output(self.COLS[bit], GPIO.LOW)
            GPIO.output(self.ROWS[bit], GPIO.LOW)

    def drawRow(self, row_string, row_index):
        self.clear()
        GPIO.output(self.ROWS[row_index], GPIO.HIGH)
        for bit in range(0, 8):
            GPIO.output(
                # column must be set to LOW to be be lit up :)
                self.COLS[bit], GPIO.HIGH if row_string[bit] == "0" else GPIO.LOW)
        time.sleep(self.sleeptime)

    def drawMatrix(self, matrix):
        for bit in range(0, 8):
            self.drawRow(matrix[bit], bit)

    def demo(self):
        cntr = 0
        while cntr < 10000:
            cntr = cntr + 1
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


def main():
    ledobj = led57_object()
    ledobj.demo()


if __name__ == "__main__":
    main()
