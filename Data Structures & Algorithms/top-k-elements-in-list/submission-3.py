class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, cnt in count.items():
            freq[cnt].append(num)
        result = []
        for i in range(len(freq)-1, 0, -1):
            if len(freq[i]) != 0:
                for x in freq[i]:
                    if len(result) == k:
                        return result
                    result.append(x)
        return result
