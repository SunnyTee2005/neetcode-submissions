class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 關鍵想法（寫進 repo）：按位置由近到遠排，比抵達時間；比前面車隊慢才算新車隊。
        cars = sorted(zip(position, speed), reverse=True)
        st = []
        for p, s in cars :
            t = (target - p) / s
            if len(st) == 0 or st[-1] < t :
                st.append(t)
            # else: 後車t<=st[-1], 直接融入
        return len(st)
        

        