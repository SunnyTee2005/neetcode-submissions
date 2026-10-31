class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        dic = { "(": ")", "[": "]", "{": "}"}
        for c in s :
            #if not len(st) and 
            if c in "([{" :
                st.append(c)
            elif not len(st) or dic[st.pop()] != c :
                return False
        return (not len(st))
        