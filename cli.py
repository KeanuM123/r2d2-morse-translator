# cli.py

from translator import lettersToMorseCode, morseCodeToLetters
from sound import play_morse_code

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
