class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [1,4,3,2]
        # because piles.length <= h, so...
        # ans scope: 1 ~ max(piles)
        # to find ans...
        # simply use binary search to find the answer
        # save min_k, and after b-search ended, return it
        # piles=[25,10,23,4]
        # h=4
        min_k = max(piles) #o(n)
        l = 1
        r = min_k
        while l <= r :
            mid = (l + r) // 2
            tmp = 0
            for i in range(len(piles)) :
                tmp += math.ceil( piles[i] / mid )
            if tmp > h :
                l = mid + 1
            else :
                r = mid - 1
                min_k = min(min_k, mid)
        return min_k
                


        