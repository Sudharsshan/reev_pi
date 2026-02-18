import board
import busio
import time
from adafruit_pca9685 import PCA9685

# Initialize I2C and PCA9685
i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)
pca.frequency = 1500

print("Starting 0-4096-0 cycle. Press Ctrl+C to stop.")

try:
    while True:
        # Ramp Up: 0 to 4096
        # We use 65535 as the max for the 16-bit library duty_cycle
        print("Ramping up...")
        pca.channels[15].duty_cycle = 4096
        time.sleep(2)

        # Ramp Down: Back to 0
        print("Ramping down...")
        pca.channels[15].duty_cycle = 0
        time.sleep(2)

except KeyboardInterrupt:
    # Clean exit: Turn off the channel
    pca.channels[15].duty_cycle = 0
    pca.deinit()
    print("\nProgram stopped and channel cleared.")
