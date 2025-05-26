# translator.py
#  This module handles translation between text and Morse code.
#  Vital for sending secret messages through the galaxy.

MORSE_CODE_DICT = {
    #  Letters A-Z
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.',  'F': '..-.', 'G': '--.',  'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--', 'N': '-.',   'O': '---',  'P': '.--.',
    'Q': '--.-','R': '.-.', 'S': '...',  'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--','Z': '--..',
      #  Numbers 0-9
    '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----',
      #  Punctuation
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-', '!': '-.-.--',
    "'": '.----.', ' ': '/'
}

#  Flip keys/values to decode Morse back to text
INVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def lettersToMorseCode(text):
    """
     Convert plain text to Morse code.
    Use this to send encrypted transmissions to the Resistance.
    """
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)

def morseCodeToLetters(code):
    """
     Convert Morse code back to human-readable text.
    Critical for decoding intercepted Empire transmissions.
    """
    return ''.join(INVERSE_MORSE_CODE_DICT.get(char, '') for char in code.split(' '))
