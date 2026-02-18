import time
import board
import busio
from adafruit_mlx90614 import MLX90614

# We use the new software I2C bus we created (Bus 3)
# In Adafruit terms, we point it to the GPIOs we defined
i2c = busio.I2C(board.D24, board.D23) # SCL, SDA
mlx = MLX90614(i2c)

def get_temp():
    try:
        ambient = mlx.ambient_temperature
        target = mlx.object_temperature
        print(f"--- Sensor Report ---")
        print(f"Ambient: {ambient:.2f}°C")
        print(f"Object:  {target:.2f}°C")
        
        if target > 100:
            print("Status: Boiling or Error!")
    except Exception as e:
        print(f"Error reading sensor: {e}")

while True:
    get_temp()
    time.sleep(1)
