import unittest

from translator import english_to_french, english_to_german

class TestEnglish(unittest.TestCase):
    def englishLanguage(self):
        self.assertEqual(english_to_french(englishTxt1=''), 'Hello')
        self.assertEqual(english_to_french(englishTxt1=''), 'Bonjour')


class TestGerman(unittest.TestCase):
    def germanLanguage(self):
        self.assertEqual(english_to_german(englishTxt2=''))
        self.assertEqual(english_to_german(englishTxt2=''))

unittest.main()
