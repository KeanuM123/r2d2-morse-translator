# gui.py
#  Desktop GUI app using Tkinter.
# Even a protocol droid could use this interface.
import tkinter as tk
from translator import lettersToMorseCode, morseCodeToLetters
from sound import play_morse_code

def encode():
    msg = input_text.get()
    result = lettersToMorseCode(msg)
    output_text.set(result)
    play_morse_code(result)

def decode():
    msg = input_text.get()
    result = morseCodeToLetters(msg)
    output_text.set(result)

#  GUI Layout
root = tk.Tk()
root.title("R2-D2 Morse Code Translator")

input_text = tk.StringVar()
output_text = tk.StringVar()

tk.Label(root, text="Input").pack()
tk.Entry(root, textvariable=input_text, width=50).pack()

tk.Button(root, text="Encode", command=encode).pack()
tk.Button(root, text="Decode", command=decode).pack()

tk.Label(root, text="Output").pack()
tk.Entry(root, textvariable=output_text, width=50).pack()

root.mainloop()
