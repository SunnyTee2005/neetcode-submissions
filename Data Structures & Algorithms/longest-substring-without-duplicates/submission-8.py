class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # abba
        st = set()
        max_len = 0
        left = 0
        for p in range(len(s)) :
            while s[p] in st :
                st.remove(s[left])
                left += 1
            st.add(s[p])
            max_len = max(max_len, p - left + 1)
        return max_len
        