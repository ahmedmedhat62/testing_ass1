import unittest
from typing import List
import collections
from unittest.mock import MagicMock

# Define the Solution class that implements the groupAnagrams method
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary that maps tuples of character counts to lists of anagrams
        ans = collections.defaultdict(list)
        for s in strs:
            # Count the occurrences of each character in the string
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            # Add the string to the list of anagrams with the same character count
            ans[tuple(count)].append(s)
        # Return a list of lists containing the anagram groups
        return list(ans.values())

# Define the TestSolution class that contains the test cases for the Solution class
class TestSolution(unittest.TestCase):
    def setUp(self):
        # Initialize test data that is used by multiple test cases
        self.solution = Solution()
        self.max_length_input = ["a" * 100] * 100
        self.expected_max_length_output = [["a" * 100] * 100]

    def tearDown(self):
        # Clean up any resources that were allocated during testing
        pass
    
    def test_empty_input(self):
        # Test that the method correctly handles an empty input list
        self.assertEqual(self.solution.groupAnagrams([]), [])

    def test_single_word_input(self):
        # Test that the method correctly handles a single-word input list
        self.assertEqual(self.solution.groupAnagrams(["abc"]), [["abc"]])

    def test_multiple_groups(self):
        # Test that the method correctly groups anagrams in a small input list
        input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected_output = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        actual_output = self.solution.groupAnagrams(input_strs)
        self.assertEqual(len(expected_output), len(actual_output))
        for group in expected_output:
            # Check that each expected anagram group is present in the actual output
            self.assertTrue(any(set(group) == set(a_group) for a_group in actual_output))

    def test_case_sensitivity(self):
        # Test that the method correctly treats uppercase and lowercase letters as distinct characters
        input_strs = ["a", "A"]
        expected_output = [["a"], ["A"]]
        actual_output = self.solution.groupAnagrams(input_strs)
        self.assertEqual(len(expected_output), len(actual_output))
        for group in expected_output:
            # Check that each expected anagram group is present in the actual output
            self.assertTrue(any(set(group) == set(a_group) for a_group in actual_output))

    def test_single_character_input(self):
        # Test that the method correctly handles input strings of length 1
        input_strs = ["a", "b", "c"]
        expected_output = [["a"], ["b"], ["c"]]
        actual_output = self.solution.groupAnagrams(input_strs)
        self.assertEqual(len(expected_output), len(actual_output))
        for group in expected_output:
            # Check that each expected anagram group is present in the actual output
            self.assertTrue(any(set(group) == set(a_group) for a_group in actual_output))

    def test_max_length_input(self):
        # Test that the method correctly handles input strings of maximum length (100)
        actual_output = self.solution.groupAnagrams(self.max_length_input)
        self.assertEqual(len(self.expected_max_length_output), len(actual_output))
        for group in self.expected_max_length_output:
            # Check that each expected anagram group is present in the actual output
            self.assertTrue(any(set(group) == set(a_group) for a_group in actual_output))
