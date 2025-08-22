import unittest
from main import suma

class TestPrueba(unittest.TestCase):


    def test_suma(self):
        self.sassertEqual(suma(2, 3), 5)