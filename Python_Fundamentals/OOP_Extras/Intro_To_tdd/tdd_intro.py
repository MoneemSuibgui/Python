import unittest
import math

#### tdd_intro Assignment Objectives: ###
##the purpose of this assignment, do all of these in a single Python file.

# 1. Write a reverseList function and test it with at least 3 cases

# 2. Write an isPalindrome function and test it with at least 5 cases

# 3.  Write a coins function and test it with at least 5 cases

# 4. BONUS: Write a recursive factorial function and test it with at least 3 cases

# 5. BONUS: Write a recursive fibonacci function and test it with at least 3 cases

def reverseList(array) :
    for i in range (math.floor(len(array)/2)):
        array[i], array[len(array)-1-i] = array[len(array)-1-i], array[i]
    return array

def isPalindrome (values) :
    if type(values) == str :
        values = str.upper(values)
    if len (values) <= 1 :
        return True
    left = 0
    right = len (values) -1
    if values [left] == values [right] :
        remainder = values [left + 1 : right]
        return isPalindrome (remainder)
    return False 

def fibonacci (n) :
    if n == 1 or n == 2 :
        return 1
    return fibonacci (n-1) + fibonacci (n-2)

def factorial (n) :
    if n < 0 :
        raise ValueError ("n must be >= 0")
    if n==0 or n==1 :
        return 1
    return n*factorial(n-1)

class ReverseListTest(unittest.TestCase) :
    def testOne(self) :
        self.assertEqual(reverseList([3,5,11,4]), [4,11,5,3])
    def testTwo(self) :
        self.assertEqual(reverseList([3,5,11,4,7]), [7,4,11,5,3])
    def testThree(self) :
        self.assertEqual(reverseList([3,5,11,4,7,7,9]), [9,7,7,4,11,5,3])
    def setUp(self) -> None:
        return super().setUp()
    def tearDown(self) -> None:
        return super().tearDown()

class IsPalindromeTests(unittest.TestCase) :
    def testOne(self) :
        self.assertEqual(isPalindrome("Abba"), True)
    def testTwo(self) :
        self.assertTrue(isPalindrome("RaceCar"))
    def testThree(self) :
        self.assertFalse(isPalindrome("rabcr"))
    def testFour(self):
        self.assertIs(isPalindrome([1, 2, 3, 4, 3, 2, 1]), True)
    def testFive(self) :
        self.assertTrue(isPalindrome((1, 2, 3, 4, 3, 2, 1)))
    def setUp(self) -> None:
        return super().setUp()
    def tearDown(self) -> None:
        return super().tearDown()

class FibonacciTests(unittest.TestCase) :
    def testOne(self) :
        self.assertEqual(fibonacci(5), 5)
    def testTwo(self) :
        self.assertIs(fibonacci(5), 5)
    def testThree(self) :
        self.assertEqual(fibonacci(4), 3)
    def setUp(self) -> None:
        return super().setUp()
    def tearDown(self) -> None:
        return super().tearDown()

class FactorialTests(unittest.TestCase) :
    def testOne(self) :
        self.assertEqual(factorial(5), 120)
    def testTwo(self) :
        self.assertIs(factorial(5), 120)
    def testThree(self) :
        self.assertEqual(factorial(4), 24)
    def setUp(self) -> None:
        return super().setUp()
    def tearDown(self) -> None:
        return super().tearDown()

if __name__ == '__main__' :
    unittest.main()