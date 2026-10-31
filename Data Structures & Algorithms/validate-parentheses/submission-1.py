class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in range(len(s)) :
            if s[i] in "([{" :
                st.append(s[i])
            elif len(st) != 0 :
                if s[i] == ")" and st.pop() != "(" :
                    return False
                elif s[i] == "]" and st.pop() != "[" :
                    return False
                elif s[i] == "}" and st.pop() != "{" :
                    return False
            else :
                return False
        return (not len(st))

        