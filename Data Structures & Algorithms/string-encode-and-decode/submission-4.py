class Solution:

    def encode(self, strs):
        result = ""
        for s in strs:
            result += str(len(s))+"#"+s
        return result
    def decode(self, sentence):
        result = []
        while sentence:
            len_of_word = ""
            for x in sentence:
                if x=="#":
                    result.append(sentence[1:int(len_of_word)+1])
                    sentence = sentence[int(len_of_word)+1:]
                    break
                len_of_word+=x
                sentence = sentence[1:]
        return result
