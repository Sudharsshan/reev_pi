import time
import board
import bitbangio
from adafruit_mlx90614 import MLX90614

# We switch from busio (Hardware) to bitbangio (Software)
# This ignores the "No Hardware I2C" error.
# SCL is Pin 18 (GPIO 24), SDA is Pin 16 (GPIO 23)
i2c = bitbangio.I2C(board.D24, board.D23, frequency=10000) # Lowered to 10kHz for stability

try:
    mlx = MLX90614(i2c)
    print("MLX90614 Link Established!")
except Exception as e:
    print(f"Failed to initialize sensor: {e}")
    print("Check your wiring on Physical Pins 16 & 18!")
    exit()

def get_temp():
    try:
        ambient = mlx.ambient_temperature
        target = mlx.object_temperature
        print(f"Ambient: {ambient:.2f}°C | Object: {target:.2f}°C")
    except Exception as e:
        print(f"Read error: {e}")

while True:
    get_temp()
    time.sleep(1)
