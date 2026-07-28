class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differenceHashMap = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in differenceHashMap:
                return [differenceHashMap[difference], index]
            differenceHashMap[num] = index
