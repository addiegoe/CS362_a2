# A2: TDD Testing hands-on
# Author: Emily Addiego
# Due Date: 11/9/20

import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    def test1(self):
        input = ""
        self.assertFalse(check_pwd(input))

    def test2(self):
        input = "hlhlfhglakfghklfadghffzgs"
        self.assertFalse(check_pwd(input))

    def test3(self):
        input = "BANANANA"
        self.assertFalse(check_pwd(input))

    def test4(self):
        input = "bananaananaaa"
        self.assertFalse(check_pwd(input))
        


if __name__ == '__main__':
    unittest.main()

