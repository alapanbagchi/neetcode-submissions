class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_frequency = {}
        for num in nums:
            num_frequency[num] = num_frequency.get(num, 0) + 1
        
        buckets = [[] for _ in range(0, len(nums))]
        for num, freq in num_frequency.items():
            buckets[freq-1].append(num)
        result = list()
        for i in range(len(buckets)-1, -1, -1):
            if len(buckets[i]) == 0:
                continue
            else:
                result.extend(buckets[i])
            if len(result) == k:
                return result
