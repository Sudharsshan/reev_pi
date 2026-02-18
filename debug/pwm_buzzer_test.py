import board
import busio
import time
from adafruit_pca9685 import PCA9685

# Hardware Setup
i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)
pca.frequency = 1500 # High frequency for a sharp buzz

# Constants for clarity
CHAN = 15
HIGH = 4096  # Full 16-bit duty cycle
OFF = 0
BURST_SPEED = 0.1  # Sharp 100ms pulses
GAP_DELAY = 0    # Your requested 2-second interval

print("SYSTEM STATUS: GAS LEAK DETECTED")
print("Executing Alarm Pattern: 1-1-1-1-1-1")

try:
    while True:
        # Execute the 6-pulse pattern
        for _ in range(6):
            pca.channels[CHAN].duty_cycle = HIGH
            time.sleep(BURST_SPEED)
            pca.channels[CHAN].duty_cycle = OFF
            time.sleep(BURST_SPEED)
        
        # 2-second delay interval after the sequence
        print(f"Waiting {GAP_DELAY} seconds...")
        time.sleep(GAP_DELAY)

except KeyboardInterrupt:
    pca.channels[CHAN].duty_cycle = OFF
    pca.deinit()
    print("\nAlarm Silenced.")
