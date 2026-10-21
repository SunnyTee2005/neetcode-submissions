class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a = 0
        b = len(heights) - 1
        max = 0
        while a < b :
            area = min(heights[a], heights[b]) * (b - a)
            if max < area:
                max = area
            if heights[a] <= heights[b] :
                a += 1
            else :
                b -= 1
        return max
        