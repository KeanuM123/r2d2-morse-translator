# R2-D2 Morse Code Translator

💡 A fun Python project to encode and decode Morse code messages — because even droids need to talk in secret!

## 💻 Preview
![Screenshot (62)](https://github.com/user-attachments/assets/28613f5b-91b4-40fa-84d5-478b35b14997)

This is R2-D2's Morse Code Translator running locally with sound and theme switching.

## 🔧 Features
- Convert English text to Morse code
- Convert Morse code to English
- Command Line Interface (CLI)
- Unit tests included

## 🚀 How to Run

### 1. Run the CLI
py cli.py

## 2. Run the Tests
py test_translator.py

## 🧪 Examples

lettersToMorseCode("I like you")
# => ".. / .-.. .. -.- . / -.-- --- ..-"

morseCodeToLetters(".. / .-.. .. -.- . / -.-- --- ..-")
# => "I LIKE YOU"

## 📦 File Structure

translator.py        # Main logic
cli.py               # Command-line interface
test_translator.py   # Unit tests
README.md            # This file

## 🎧 Extras

- `sound.py`: Plays Morse code as beeps
- `gui.py`: Tkinter desktop app
- `web_app.py`: Flask-powered web app

## 🛠️ Run GUI
py gui.py

## 🌐 Run Web Version

py web_app.py
# Then go to http://localhost:5000

## 📖 About

R2-D2 Morse Code Translator is a fun, multi-interface Python project inspired by the Star Wars universe. It converts plain text to Morse code and vice versa, helping R2-D2 decode secret rebel transmissions—or send encrypted jokes to C-3PO!

This project includes:

✅ A clean Python backend for encoding and decoding

🖥️ A command-line interface (CLI)

🔊 Sound effects that beep like a droid

🪟 A graphical desktop app (GUI) using Tkinter

🌐 A simple web interface built with Flask

🧪 Unit tests and full GitHub workflow

Built with readability, functionality, and fun in mind — perfect for learning about text encoding, GUIs, and Python web apps!

“Beep beep bwoop!” — R2-D2
