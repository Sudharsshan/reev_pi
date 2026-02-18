from smbus2 import SMBus, i2c_msg
import time

# Use Bus 1 for standard pins (3 & 5) or Bus 3 if you kept the dtoverlay
BUS_NUMBER = 1 
DEVICE_ADDRESS = 0x5a

def read_temp(reg):
    with SMBus(BUS_NUMBER) as bus:
        # MLX90614 requires a specific 'Repeated Start' read
        # Data is 3 bytes: Low Byte, High Byte, Pec (Error check)
        read = i2c_msg.read(DEVICE_ADDRESS, 3)
        write = i2c_msg.write(DEVICE_ADDRESS, [reg])
        
        bus.i2c_rdwr(write, read)
        
        data = list(read)
        # Formula: (Data * 0.02) - 273.15 (Kelvin to Celsius)
        temp = ((data[1] << 8) | data[0]) * 0.02 - 273.15
        return temp

try:
    while True:
        # 0x07 is the register for Object Temperature
        # 0x06 is the register for Ambient Temperature
        obj_temp = read_temp(0x07)
        amb_temp = read_temp(0x06)
        
        print(f"Object: {obj_temp:.2f}°C | Ambient: {amb_temp:.2f}°C")
        time.sleep(1)
        
except Exception as e:
    print(f"Tech failure: {e}")
