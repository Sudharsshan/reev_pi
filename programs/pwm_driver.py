import time
import json
import board
import busio
from adafruit_pca9685 import PCA9685

# ------------------ INIT ------------------

i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c, address=0x40)

pca.frequency = 1200  # Global PWM frequency

BUZZER_CHANNEL = 15
TIME_SLICE = 0.25  # seconds per pattern step

# ------------------ PATTERNS ------------------

BUZZER_PATTERNS = {
    "GAS_LEAK":        [1,1,1,1,1,1],
    "BATTERY_SOC_LOW": [1,0,1,0,1,0,1,0],
    "BATTERY_HIGH_T":  [1,1,0,1,1,0,1,1,0],
    "PI_ERROR":        [1,1,0,0,1,1,0,0],
    "SENSOR_ERROR":    [1,0,0,0,1,0,0,0,1]
}

# ------------------ HELPERS ------------------

def set_led(channel, value):
    """
    value: 0–4095
    """
    pca.channels[channel].duty_cycle = value

def buzzer_on():
    pca.channels[BUZZER_CHANNEL].duty_cycle = 2048  # 50%

def buzzer_off():
    pca.channels[BUZZER_CHANNEL].duty_cycle = 0

def play_buzzer_pattern(pattern_name):
    pattern = BUZZER_PATTERNS.get(pattern_name)
    if not pattern:
        print("Unknown buzzer pattern")
        return

    for step in pattern:
        if step == 1:
            buzzer_on()
        else:
            buzzer_off()
        time.sleep(TIME_SLICE)

    buzzer_off()

# ------------------ COMMAND INTERPRETER ------------------

def process_command(command):
    for lane, value in command:
        if lane == BUZZER_CHANNEL:
            play_buzzer_pattern(value)
        else:
            set_led(lane, int(value))

# ------------------ TEST ------------------

if __name__ == "__main__":
    test_json = '''
    [
        [0, 0],
        [1, 0],
        [2, 0],
        [3, 0],
        [4, 0],
        [5, 0],
        [15, "BATTERY_SOC_LOW"]
    ]
    '''

    command = json.loads(test_json)
    process_command(command)
