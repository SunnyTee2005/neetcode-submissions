class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use hashmap for sure.
        # compare str length first
        if len(s) != len(t) : return False

        # if str 's' and 't' has the same length, there number of keys in hashmap should also be equal.
        # Each string has it's own hashmap, save chars as keys(attributes in this case) and the number of occurence as value.
        countS = {}
        countT = {}
        # Fill in the hashmap first
        for c in range(len(s)) :
            countS[s[c]] = countS.get(s[c], 0) + 1
            countT[t[c]] = countT.get(t[c], 0) + 1
        # Compare the values in the hashmap of two strings.
        for c in range(len(s)) :
            if countS[s[c]] != countT.get(s[c], 0) :
                return False
        
        return True