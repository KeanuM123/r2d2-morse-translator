# sound.py
#  Generates beeps for Morse code using built-in sound.
# Used for droid-style communication or secret alerts.

import winsound
import time

DOT_DURATION = 100  # milliseconds    # ⏱ Duration of a dot (short beep)
DASH_DURATION = DOT_DURATION * 3     # ⏱ Duration of a dash (long beep)
FREQUENCY = 750  # Hz               #  Sound pitch in Hz


def beep_for_symbol(symbol):
    """
     Interpret each Morse symbol and play the correct sound.
    """
    if symbol == '.':
        winsound.Beep(FREQUENCY, DOT_DURATION)
    elif symbol == '-':
        winsound.Beep(FREQUENCY, DASH_DURATION)
    elif symbol == '/':
        time.sleep(0.7)
    elif symbol == ' ':
        time.sleep(0.2)

def play_morse_code(morse_code):
    """
     Play Morse code message one beep at a time.
    Use when transmitting stealth messages to nearby allies.
    """
    for char in morse_code:
        beep_for_symbol(char)
        time.sleep(0.1)  # brief pause between beeps
