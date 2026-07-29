class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string))+"#"+string
        return result
        
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length_of_str = int(s[i:j])
            i = j + 1
            result.append(s[i:i+length_of_str])
            i+=length_of_str
        return result
