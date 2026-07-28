class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_frequency = [0]*26
        for x in s:
            char_frequency[ord(x)-97] += 1
        for s in t:
            char_frequency[ord(s)-97] -= 1
        for i in char_frequency:
            if i != 0:
                return False
        return True
            
        
        