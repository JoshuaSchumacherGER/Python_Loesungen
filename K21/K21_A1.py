from ast import Assert
from cmath import sqrt
import unittest

class TestObject:
    def is_empty_list(__container: list):
        return True if len(__container) == 0 else False
        
    def square_root(__arg):
        return sqrt(__arg)
        
class BaseTest(unittest.TestCase):
    def test_is_empty_list(self):
        test_container = [([], True), 
                          ([1, 2, 3], False), 
                          ([], True), 
                          ([5], False)]
        for test in test_container:
            self.assertEqual(TestObject.is_empty_list(test[0]) == test[1], True)
            
    def test_square_root(self):
        test_container = [(4, 2),
                          (9, 3),
                          (16, 4),
                          (25, 5),
                          (100, 10),
                          (121, 11),
                          (256, 16)]
        for test in test_container:
            self.assertEqual(TestObject.square_root(test[0]) == test[1], True)
         
unittest.main()

