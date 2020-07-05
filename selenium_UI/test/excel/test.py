#encoding:utf-8

import unittest

class Test_php(unittest.TestCase):

    def test_run(self):
        a = 1
        b = 2
        c = a+b
        self.assertEqual(a+b,c,'error!')


if __name__ == '__main__':
    unittest.main()