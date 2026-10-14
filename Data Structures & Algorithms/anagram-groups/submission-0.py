class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for s in strs :
            arr = [0] * 26
            for i in range(len(s)) :
                arr[ ord(s[i]) - ord('a') ] += 1
            map[tuple(arr)].append(s)
        ans = []
        for v in map.values() :
            ans.append(v)
        return ans
            