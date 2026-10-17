class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = 0
        b = len(s) - 1
        s = s.lower()
        # s="Ww"
        while a < b :
            if not (s[a].isalpha() or s[a].isnumeric()) :
                a += 1
            elif not (s[b].isalpha() or s[b].isnumeric()) :
                b -= 1
            elif s[a] == s[b] :
                a += 1
                b -= 1
            else :
                return False
        return True