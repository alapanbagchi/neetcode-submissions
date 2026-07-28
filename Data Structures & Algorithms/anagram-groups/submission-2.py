class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = defaultdict(list)
        for x in strs:
            count = [0] * 26
            for y in x:
                count[ord(y)-ord('a')] += 1
            freq_map[tuple(count)].append(x)
        return freq_map.values()