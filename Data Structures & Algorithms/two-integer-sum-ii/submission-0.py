class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        b = len(numbers) - 1
        ans = []
        while a < b :
            if numbers[a] + numbers[b] > target :
                b -= 1
            elif numbers[a] + numbers[b] < target :
                a += 1 
            else :
                ans.append(a+1)
                ans.append(b+1)
                break
        return ans

        