import math
import unittest
from pathing import get_middle_path
from collections import deque
from pathing import get_dfs_path
from pathing import get_bfs_path
from permutation import stepOne
from permutation import findLargestMobileVariable
from permutation import StepThreeSwap
from permutation import StepFourSwitch
from permutation import allPermutations


class TestSJTAlgorithm(unittest.TestCase):

   def test_stepOne(self):
        perm, directions = stepOne(3)
        self.assertEqual(perm, [1, 2, 3])
        self.assertEqual(directions, [-1, -1, -1])

   def test_findLargestMobileVariable(self):
        perm = [2, 1, 3]
        directions = [-1, -1, -1]
        index = findLargestMobileVariable(3, perm, directions)
        self.assertEqual(index, 2) 
     
   def test_no_mobile_integers(self):
        # Set up a permutation where no integers are mobile
        perm = [1, 2, 3]        # Permutation
        directions = [1, 1, 1]  # All directed to the right
        
        result = findLargestMobileVariable(len(perm), perm, directions)
        self.assertEqual(result, -1)  


   def test_stepThreeSwap(self):
        perm = [3, 1, 2]
        directions = [-1, -1, -1]
        largest_mobile_index = 0
        StepThreeSwap(perm, directions, largest_mobile_index)
        self.assertEqual(perm, [2,1,3])  # Expected after swap
        self.assertEqual(directions, [-1, -1, -1])  # Directions remain unchanged

   def test_stepFourSwitch(self):
        perm = [1, 3, 2]
        directions = [-1, -1, -1]
        mobile_value = 3
        updated_directions = StepFourSwitch(perm, directions, mobile_value)
        self.assertEqual(updated_directions, [-1, -1, -1])  # Only the direction of 3 should change

#    def test_sjt_algorithm(self):
#         permutations = allPermutations(4)
#         expected_permutations = [[1, 2, 3], [1, 3, 2], [3, 1, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1]]
#         self.assertEqual(permutations, expected_permutations)

   def test_all_permutations_n_3(self):
        permutations = allPermutations(3)
        expected_permutations = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ]
        self.assertEqual(permutations, expected_permutations)



if __name__ == '__main__':
    unittest.main()
