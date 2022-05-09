"""
Kapitel 21
Author: Ali Abas Arsalahn
Datum: 02.05.2022
"""


import unittest
from listcheck import ListCheckAndSQRT


class TestListCheckAndSQRT(unittest.TestCase):
    """Testklasse für ListCheckAndSQRT"""

    def setUp(self) -> None:
        self.test_objekt = ListCheckAndSQRT()

    def tearDown(self) -> None:
        pass

    def test_is_empty_list(self) -> None:
        """Test für is_empty_list"""
        self.assertTrue(self.test_objekt.is_empty_list([]))
        self.assertFalse(self.test_objekt.is_empty_list([-1]))
        with self.assertRaises(TypeError):
            self.test_objekt.is_empty_list({})

    def test_squareroot(self) -> None:
        """Test für ListCheckAndSQRT.squareroot()"""
        self.assertEqual(self.test_objekt.squareroot(16), 4)
        with self.assertRaises(ValueError):
            self.test_objekt.squareroot(-1)


if __name__ == '__main__':
    unittest.main()
