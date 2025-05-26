# cli.py

from translator import lettersToMorseCode, morseCodeToLetters

def main():
    choice = input("Type 'E' to encode or 'D' to decode: ").strip().upper()
    if choice == 'E':
        msg = input("Enter text to encode: ")
        print("Morse Code:", lettersToMorseCode(msg))
    elif choice == 'D':
        code = input("Enter Morse to decode: ")
        print("Text:", morseCodeToLetters(code))
    else:
        print("Invalid choice. Use 'E' or 'D'.")

if __name__ == "__main__":
    main()
