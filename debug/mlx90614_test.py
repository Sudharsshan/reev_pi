import RPi.GPIO as GPIO
import time

# ---------------- CONFIG ----------------
SCL = 23
SDA = 24
MLX_ADDR = 0x5A
DELAY = 0.0005  # 5 microseconds (slow + stable)
# ----------------------------------------

GPIO.setmode(GPIO.BCM)
GPIO.setup(SCL, GPIO.OUT)
GPIO.setup(SDA, GPIO.OUT)

def sda_high():
    GPIO.setup(SDA, GPIO.IN)

def sda_low():
    GPIO.setup(SDA, GPIO.OUT)
    GPIO.output(SDA, GPIO.LOW)

def scl_high():
    GPIO.output(SCL, GPIO.HIGH)

def scl_low():
    GPIO.output(SCL, GPIO.LOW)

def i2c_delay():
    time.sleep(DELAY)

def start():
    sda_high()
    scl_high()
    i2c_delay()
    sda_low()
    i2c_delay()
    scl_low()

def stop():
    sda_low()
    scl_high()
    i2c_delay()
    sda_high()
    i2c_delay()

def write_bit(bit):
    if bit:
        sda_high()
    else:
        sda_low()
    i2c_delay()
    scl_high()
    i2c_delay()
    scl_low()

def read_bit():
    sda_high()
    i2c_delay()
    scl_high()
    bit = GPIO.input(SDA)
    i2c_delay()
    scl_low()
    return bit

def write_byte(byte):
    for i in range(8):
        write_bit((byte << i) & 0x80)
    return not read_bit()  # ACK = 0

def read_byte(ack=True):
    val = 0
    for _ in range(8):
        val = (val << 1) | read_bit()
    write_bit(0 if ack else 1)
    return val

def smbus_read_word(cmd):
    start()
    if not write_byte((MLX_ADDR << 1) | 0):
        raise IOError("No ACK on address (write)")
    if not write_byte(cmd):
        raise IOError("No ACK on command")

    sda_high()
    scl_high()
    i2c_delay()
    time.sleep(0.010) # MLX internal processing time

    start()
    write_byte((MLX_ADDR << 1) | 1)

    low = read_byte(ack=True)
    high = read_byte(ack=True)
    _pec = read_byte(ack=False)  # PEC ignored

    stop()
    return (high << 8) | low

def temp_from_raw(raw):
    return raw * 0.02 - 273.15

try:
    ambient_raw = smbus_read_word(0x06)
    object_raw  = smbus_read_word(0x07)

    print(f"Ambient Temp : {temp_from_raw(ambient_raw):.2f} °C")
    print(f"Object Temp  : {temp_from_raw(object_raw):.2f} °C")
    print(hex(smbus_read_word(0x3C)))

finally:
    GPIO.cleanup()
