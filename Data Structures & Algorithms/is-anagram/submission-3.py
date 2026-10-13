class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for c in s :
            dic[c] = dic.get(c, 0) + 1
        for c in t :
            dic[c] = dic.get(c, 0) - 1
        for key in dic :
            if dic[key] != 0 :
                return False
        return True