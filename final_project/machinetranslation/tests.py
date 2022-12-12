import unittest
from translator import *


class TestEnglishToFrench(unittest.TestCase):

    def test_english_translate(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertIsNotNone(english_to_french(""), "")

    def test_french_translate(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertIsNotNone(french_to_english(""), "")


if __name__ == '__main__':
    unittest.main()
