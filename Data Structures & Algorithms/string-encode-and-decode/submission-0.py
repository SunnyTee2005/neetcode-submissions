class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for i in strs :
            length = len(i)
            ret += f"{length}#{i}"
        return ret
    def decode(self, s: str) -> List[str]:
        # str.find("str", index)
        # slicing str[x : y], contains chars from x to (y-1)
        # int() : ascii to integer
        # "5#Hello5#World"
        out = []
        i = 0 # 5
        while (i + 1) < len(s) :
            tmp = s.find("#", i) # 7
            length_str = s[i : tmp]
            target_length = int(length_str) # number of chars in current string 
            target_str = s[ (tmp + 1) : (tmp + 1 + target_length) ]
            out.append(target_str)
            i = tmp + target_length + 1
        return out


