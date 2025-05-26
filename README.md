# R2-D2 Morse Code Translator

💡 A fun Python project to encode and decode Morse code messages because even droids need to talk in secret!

## 🔧 Features
- Convert English text to Morse code
- Convert Morse code to English
- Command Line Interface (CLI)
- Unit tests included

## 🚀 How to Run

### 1. Run the CLI
py cli.py

2. Run the Tests
py test_translator.py

🧪 Examples
lettersToMorseCode("I like you")
# => ".. / .-.. .. -.- . / -.-- --- ..-"

morseCodeToLetters(".. / .-.. .. -.- . / -.-- --- ..-")
# => "I LIKE YOU"

📦 File Structure
translator.py        # Main logic
cli.py               # Command-line interface
test_translator.py   # Unit tests
README.md            # This file