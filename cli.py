# cli.py

from translator import lettersToMorseCode, morseCodeToLetters

def main():
    print("💬 R2-D2 Morse Code Translator")
    print("Choose an option:")
    print(" [E] Encode")
    print(" [D] Decode")
    print(" [Q] Quit")

    while True:
        choice = input("\nYour choice: ").strip().upper()

        if choice == 'E':
            msg = input("Enter message to encode: ")
            print("📤 Morse Code:", lettersToMorseCode(msg))
        elif choice == 'D':
            code = input("Enter Morse Code to decode: ")
            print("📥 Decoded Text:", morseCodeToLetters(code))
        elif choice == 'Q':
            print("👋 Goodbye, human!")
            break
        else:
            print("❌ Invalid choice. Use E, D, or Q.")

if __name__ == "__main__":
    main()
