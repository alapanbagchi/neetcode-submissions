class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFrequency = {}
        for num in nums:
            if num in numFrequency:
                numFrequency[num] = numFrequency[num] + 1
            else:
                numFrequency[num] = 1
        numFrequencySorted = dict(sorted(numFrequency.items(), key=lambda x:x[1], reverse=True))
        print(numFrequencySorted)
        return list(numFrequencySorted.keys())[:k]
