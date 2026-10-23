class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "abcabcbb"
        # s="dvdf"
        left = 0
        right = 0
        max_count = 0
        mp = {}
        for right in range(len(s)) :
            if s[right] not in mp :
                mp[ s[right] ] = right
            else : # in mp
                left = max(left, mp[s[right]] + 1)
                mp[ s[right] ] = right
            max_count = max(max_count, right-left+1)
        return max_count

        
                    
