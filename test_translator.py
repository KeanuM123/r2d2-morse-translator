# test_translator.py

import unittest
from translator import lettersToMorseCode, morseCodeToLetters

class TestMorseTranslator(unittest.TestCase):
    def test_letters_to_morse(self):
        self.assertEqual(lettersToMorseCode("SOS"), "... --- ...")
        self.assertEqual(lettersToMorseCode("I like you"), ".. / .-.. .. -.- . / -.-- --- ..-")

    def test_morse_to_letters(self):
        self.assertEqual(morseCodeToLetters(".... . .-.. .-.. ---"), "HELLO")
        self.assertEqual(morseCodeToLetters(".. / .-.. .. -.- . / -.-- --- ..-"), "I LIKE YOU")

if __name__ == '__main__':
    unittest.main()
