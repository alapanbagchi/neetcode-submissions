class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res =  res + str(len(list(word))) +"#"+word
        return res

    def decode(self, s: str) -> List[str]:
        # 4#neet4#code4#love3#you
        res = []
        while len(s):
            word_length = s[0:s.index("#", 1)]
            word_start_index = s.index("#", 1) + 1
            res.append(s[word_start_index : int(word_length) + word_start_index])
            s = s[int(word_start_index) + int(word_length):]
        print(res)
        return res