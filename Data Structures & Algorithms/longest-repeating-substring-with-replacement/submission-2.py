class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # "AAABABB"
        # "ABC" k=1
        # s="AAAB" k=0
        # s="AAABABB" k=1
        max_len = 0
        mp = {}
        left = 0
        for p in range(len(s)) : 
            #if s[p] not in mp :
            #    mp[ s[p] ] = 1
            #else :
            #    mp[ s[p] ] += 1
            mp[ s[p] ] = mp.get(s[p], 0) + 1
            while k <  (p - left + 1) - max(mp.values()) :
                mp[ s[left] ] -= 1
                left += 1
            max_len = max(max_len, p-left+1)
        return max_len
        