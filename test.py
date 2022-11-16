import unittest

class  Fizzbuzz(unittest.TestCase):
    def test_1(self):
        Fizzbuzz(1)
    def  test_1(self):
        self.assertEqual(FizzBuzz(3),"buzz")
    def test_a(self):
        self.assertEqual(FizzBuzz(5),"fizz")
    def test_f(self):
        self.assertEqual(FizzBuzz(15),"fizzbuzz")


def FizzBuzz(a):
    if(a == 3):
        return "buzz"
    elif(a%5 == 0):
        return "fizz"
unittest.main()
