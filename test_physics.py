import unittest
from physics import PhysicsCaluslator 

class TestPhysicsCaluslator(unittest.TestCase):

    def test_calculate_force(self):
        calc = PhysicsCaluslator()
        self.assertEqual(calc.calculate_force(10,2), 20)

    def test_zero_mass(self):
        calc = PhysicsCaluslator()
        self.assertEqual(calc.calculate_force(0,10), 0)

if __name__=='__main__':
    unittest.main()