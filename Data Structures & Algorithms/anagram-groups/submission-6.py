class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = dict()
        for index, word in enumerate(strs):
            word_frequency = [0]*26
            for letter in word:
                word_frequency[ord(letter) - ord('a')] += 1
            key = tuple(word_frequency)
            print(key)
            if key in anagram_map:
                anagram_map[key].append(word)
            else:
                anagram_map[key] = [word]
        
        return list(anagram_map.values())
            
