import unittest
from min_extra_char_trie import minExtraChar

class TestMinExtraChar(unittest.TestCase):
    def test_case_1(self):
        s = "leetscode"
        dictionary = ["leet", "code"]
        self.assertEqual(minExtraChar(s, dictionary), 1)

    def test_case_2(self):
        s = "applebanana"
        dictionary = ["apple", "banana"]
        self.assertEqual(minExtraChar(s, dictionary), 0)

    def test_case_3(self):
        s = "applebananax"
        dictionary = ["apple", "banana"]
        self.assertEqual(minExtraChar(s, dictionary), 1)

    def test_case_4(self):
        s = "abcdefg"
        dictionary = ["hij", "klm"]
        self.assertEqual(minExtraChar(s, dictionary), 7)

    def test_case_5(self):
        s = "appleappleapple"
        dictionary = ["apple"]
        self.assertEqual(minExtraChar(s, dictionary), 0)

if __name__ == '__main__':
    unittest.main()