class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(NlogN)
        ans = []
        for i in range(0, len(nums) - 2) :
            if i > 0 and nums[i] == nums[i - 1] :
                continue
            target = -nums[i]
            a = i + 1
            b = len(nums) - 1
            while a < b :
                if nums[a] + nums[b] < target :
                    a += 1
                elif nums[a] + nums[b] > target :
                    b -= 1
                else :
                    ans.append([nums[i], nums[a], nums[b]])
                    a += 1
                    while a < b and nums[a] == nums[a-1] :
                        a += 1
                    b -= 1
        return ans

            


        