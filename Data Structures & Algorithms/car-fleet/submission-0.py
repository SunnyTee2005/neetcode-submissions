class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        st = []
        for p, s in cars :
            t = (target - p) / s
            if len(st) == 0 or st[-1] < t :
                st.append(t)
            # else: 後車t<=st[-1], 直接融入
        return len(st)
        

        