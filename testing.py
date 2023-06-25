import unittest
from typing import List
import collections
from unittest.mock import MagicMock

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.max_length_input = ["a" * 100] * 100
        self.expected_max_length_output = [["a" * 100] * 100]
        self.non_latin_input = ["こんにちは", "你好", "안녕하세요"]
        self.expected_non_latin_output = [["こんにちは"], ["你好"], ["안녕하세요"]]

    def tearDown(self):
        pass
    
    def test_empty_input(self):
        self.assertEqual(self.solution.groupAnagrams([]), [])

    def test_single_word_input(self):
        self.assertEqual(self.solution.groupAnagrams(["abc"]), [["abc"]])

    def test_multiple_groups(self):
        input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected_output = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        actual_output = self.solution.groupAnagrams(input_strs)
        self.assertEqual(len(expected_output), len(actual_output))
        for group in expected_output:
            with self.subTest(group=group):
                self.assertIn(group, actual_output)

    def test_case_sensitivity(self):
        input_strs = ["a", "A"]
        expected_output = [["a"], ["A"]]
        actual_output = self.solution.groupAnagrams(input_strs)
        self.assertEqual(len(expected_output), len(actual_output))
        for group in expected_output:
            with self.subTest(group=group):
                self.assertIn(group, actual_output)

    def test_single_character_input(self):
        input_strs = ["a", "b", "c"]
        expected_output = [["a"], ["b"], ["c"]]
        actual_output = self.solution.groupAnagrams(input_strs)
        self.assertEqual(len(expected_output), len(actual_output))
        for group in expected_output:
            with self.subTest(group=group):
                self.assertIn(group, actual_output)

    def test_max_length_input(self):
        actual_output = self.solution.groupAnagrams(self.max_length_input)
        self.assertEqual(len(self.expected_max_length_output), len(actual_output))
        for group in self.expected_max_length_output:
            with self.subTest(group=group):
                self.assertIn(group, actual_output)

    def test_non_latin_input(self):
        actual_output = self.solution.groupAnagrams(self.non_latin_input)
        self.assertEqual(len(self.expected_non_latin_output), len(actual_output))
        for group in self.expected_non_latin_output:
            with self.subTest(group=group):
                self.assertIn(group, actual_output)

    def test_higher_boundary(self):
        input_strs = ["a" * 5000] * 2000
        expected_output = [["a" * 5000] * 2000]
        actual_output = self.solution.groupAnagrams(input_strs)
        self.assertEqual(len(expected_output), len(actual_output))
        for group in expected_output:
            with self.subTest(group=group):
                self.assertIn(group, actual_output)

    def test_mock_input(self):
        mock_input = MagicMock(return_value=["eat", "tea", "tan", "ate", "nat", "bat"])
        expected_output = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        actual_output = self.solution.groupAnagrams(mock_input())
        self.assertEqual(len(expected_output), len(actual_output))
        for group in expected_output:
            with self.subTest(group=group):
                self.assertIn(group, actual_output)