class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxH = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            A = (r-l) * min(heights[l], heights[r])
            maxH = max(A, maxH)
            minH = min(heights[l], heights[r])
            if minH == heights[l]: l += 1
            else: r -= 1
        return maxH