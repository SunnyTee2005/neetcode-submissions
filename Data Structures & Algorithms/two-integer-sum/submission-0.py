class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        ans = []
        counter = 0
        for n in nums:
            if (target - n) in di:
                ans.append(counter)
                ans.append(di[target - n])
                ans.sort()
                return ans
            di[n] = counter
            counter += 1
        return ans