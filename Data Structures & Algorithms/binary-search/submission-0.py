class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target < nums[0] or nums[len(nums) - 1] < target : return -1
        head = 0
        mid = len(nums) // 2
        tail = len(nums) - 1
        
        while head <= tail :
            mid = (head + tail) // 2

            if target < nums[mid] :
                tail = mid - 1
            elif nums[mid] < target :
                head = mid + 1
            elif target == nums[mid] :
                return mid

        return -1
            

