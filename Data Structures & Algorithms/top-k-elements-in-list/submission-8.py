class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_frequency = dict()

        for num in nums:
            num_frequency[num] = num_frequency.get(num, 0) + 1
        sorted_by_freq = sorted(num_frequency.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in sorted_by_freq[:k]] 