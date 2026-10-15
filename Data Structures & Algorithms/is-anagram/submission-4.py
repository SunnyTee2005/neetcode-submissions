class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = defaultdict(str)
        for i in s :
            mp[i] = mp.get(i, 0) + 1
        for i in t :
            mp[i] = mp.get(i, 0) - 1
        
        for i in mp:
            if mp[i] != 0 :
                return False
        return True
        