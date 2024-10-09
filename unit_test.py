import math
import unittest
from pathing import get_middle_path


class TestPathFinding(unittest.TestCase):

    def setUp(self):
        self.graph = [
            [(0, 0), [1, 2]],
            [(100, 0), [0, 3]],
            [(0, 100), [0, 4]],
            [(200, 0), [1, 5]],
            [(100, 100), [2, 6]],
            [(300, 0), [3, 7]],
            [(200, 100), [4, 8]],
            [(400, 0), [5, 9]],
            [(300, 100), [6, 9]],
            [(500, 0), [7, 8]]
        ]
    
    def test_pathfinding_start_to_end(self):
        path = get_middle_path(self.graph, 0, 9)
        self.assertEqual(path[0], 0, "Path should start at index 0")
        self.assertEqual(path[-1], 9, "Path should end at index 9")

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)


if __name__ == '__main__':
    unittest.main()
