class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Area = min(height1, height2) * (index(height2) - index(height1))
        left = 0
        right = len(heights) - 1
        maxArea = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            maxArea = max(maxArea, area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea
