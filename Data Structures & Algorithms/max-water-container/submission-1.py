class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxHeight = -1
        while l < r:
            if (min(heights[l], heights[r]) * (r - l)) > maxHeight:
                maxHeight = min(heights[l], heights[r]) * (r - l)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        return maxHeight