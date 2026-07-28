class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums) 

        for i in range(len(nums)):
            if i==0:
                prefix[i] = nums[i] * 1
            else:
                prefix[i] = nums[i] * prefix[i-1]
        
        for i in range(len(nums) - 1, -1, -1):
            if i==len(nums)-1:
                postfix[i] = nums[i] * 1
            else:
                postfix[i] = nums[i] * postfix[i+1]
        res = []
        for i in range(len(nums)):
            if i==0:
                res.append(1*postfix[i+1])
            elif i == len(nums) - 1:
                res.append(prefix[i-1] * 1)
            else:
                res.append(prefix[i-1] * postfix[i+1])
        return res