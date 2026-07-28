class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_map = dict()
        for index, num in enumerate(nums):
            if target-num in difference_map:
                if index > difference_map[target-num]:
                    return [difference_map[target-num], index]
                else:
                    return [index, difference_map[target-num]]
            difference_map[num] = index