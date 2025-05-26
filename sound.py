# sound.py
import winsound
import time

DOT_DURATION = 100  # milliseconds
DASH_DURATION = DOT_DURATION * 3
FREQUENCY = 750  # Hz

def beep_for_symbol(symbol):
    if symbol == '.':
        winsound.Beep(FREQUENCY, DOT_DURATION)
    elif symbol == '-':
        winsound.Beep(FREQUENCY, DASH_DURATION)
    elif symbol == '/':
        time.sleep(0.7)
    elif symbol == ' ':
        time.sleep(0.2)

def play_morse_code(morse_code):
    for char in morse_code:
        beep_for_symbol(char)
        time.sleep(0.1)  # brief pause between beeps
