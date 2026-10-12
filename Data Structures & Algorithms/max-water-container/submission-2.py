class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left , right = 0, len(heights) - 1
        maxCapacity = 0
        
        while left < right:
            top = min(heights[left], heights[right])
            capacity = top * (right - left)
            maxCapacity = max(maxCapacity, capacity)

            if heights[left] < heights[right]:
                left += 1
            else: 
                right -= 1

        return maxCapacity