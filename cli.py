# cli.py
#  Interface for encoding and decoding from the terminal.
# Useful when the Resistance is low on UI resources.
from translator import lettersToMorseCode, morseCodeToLetters
from sound import play_morse_code

"""
     Runs an interactive loop for the user to encode or decode messages.
    Choose Encode to create a Morse message.
    Choose Decode to crack the Empire's code.
"""
def main():
    
    print("💬 R2-D2 Morse Code Translator")
    print(" [E] Encode\n [D] Decode\n [Q] Quit")

    while True:
        choice = input("\nYour choice: ").strip().upper()

        if choice == 'E':
            msg = input("Enter message to encode: ")
            morse = lettersToMorseCode(msg)
            print("📤 Morse Code:", morse)
            play_morse_code(morse)
        elif choice == 'D':
            code = input("Enter Morse Code to decode: ")
            print("📥 Decoded Text:", morseCodeToLetters(code))
        elif choice == 'Q':
            print("👋 Goodbye, human!")
            break
        else:
            print("❌ Invalid choice.")
