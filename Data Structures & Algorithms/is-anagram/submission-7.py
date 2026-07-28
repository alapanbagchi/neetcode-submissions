class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       return sorted([letter for letter in s]) == sorted([letter for letter in t])