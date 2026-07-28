class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numHash = {}
        if nums == []:
            return 0
        for num in nums:
            numHash[num] = set()
        
        for num in nums:
            curr_num = num
            while curr_num + 1 in numHash:
                numHash[num].add(curr_num + 1)
                curr_num = curr_num + 1
        lengths = [len(x) + 1 for x in list(numHash.values())]
        return max(lengths)
                
