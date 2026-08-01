class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -4, -1, -1, 0, 1, 2
        sorted_nums = sorted(nums)
        a = 0
        left = 1
        right = len(nums) - 1
        result = []
        for i, a in enumerate(sorted_nums):
            if a > 0:
                break
            if i > 0 and a == sorted_nums[i-1]:
                continue
            else:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    threesum = sorted_nums[left] + sorted_nums[right] + a
                    if threesum < 0:
                        left += 1
                    elif threesum > 0:
                        right -= 1
                    else:
                        result.append([sorted_nums[left],sorted_nums[right],a])
                        left += 1
                        right -= 1
                        while sorted_nums[left] == sorted_nums[left-1] and left < right:
                            left += 1
        return result
                  
