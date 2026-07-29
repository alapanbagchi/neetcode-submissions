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
            char_length = 0
            for j in range(i, len(s)-1):
                if s[j].isdigit():
                    char_length = char_length * 10 + int(s[j])
                else:
                    break
            i += len(str(char_length))+1
            result.append(s[i:i+char_length])
            i+=char_length
            print(i)
            char_length = 0
        return result
