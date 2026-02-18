import time
from smbus2 import SMBus, i2c_msg
import os

# Set to 3 because of your config.txt: bus=3
BUS_NUMBER = 3 
DEVICE_ADDRESS = 0x5a

def check_bus():
    if not os.path.exists(f"/dev/i2c-{BUS_NUMBER}"):
        print(f"CRITICAL ERROR: /dev/i2c-{BUS_NUMBER} not found!")
        print("Check if 'dtoverlay=i2c-gpio,bus=3...' is active in config.txt")
        return False
    return True

def read_mlx_temp(reg):
    """
    Reads from the MLX90614 using a Repeated Start condition.
    0x07 = Object Temperature
    0x06 = Ambient Temperature
    """
    try:
        with SMBus(BUS_NUMBER) as bus:
            # We need to write the register address, then immediately read 3 bytes
            # [Low Byte, High Byte, PEC (Packet Error Code)]
            write = i2c_msg.write(DEVICE_ADDRESS, [reg])
            read = i2c_msg.read(DEVICE_ADDRESS, 3)
            
            # This executes the combined write/read transaction
            bus.i2c_rdwr(write, read)
            
            data = list(read)
            
            # The Math:
            # 1. Combine High and Low bytes: (Data[1] << 8) | Data[0]
            # 2. Multiply by resolution (0.02) to get Kelvin
            # 3. Subtract 273.15 to get Celsius
            raw_temp = (data[1] << 8) | data[0]
            
            # Check for common error flag (0xFFFF)
            if raw_temp == 0xFFFF:
                return None
                
            temp_celsius = (raw_temp * 0.02) - 273.15
            return temp_celsius
    except Exception as e:
        print(f"I/O Error on Bus {BUS_NUMBER}: {e}")
        return None

if __name__ == "__main__":
    print(f"Starting MLX90614 monitor on I2C Bus {BUS_NUMBER}...")
    
    if check_bus():
        try:
            while True:
                obj = read_mlx_temp(0x07)
                amb = read_mlx_temp(0x06)
                
                if obj is not None and amb is not None:
                    print(f"Target: {obj:6.2f}°C | Ambient: {amb:6.2f}°C")
                else:
                    print("Waiting for valid sensor data...")
                
                time.sleep(0.5) # Fast refresh for a responsive gadget
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user.")
