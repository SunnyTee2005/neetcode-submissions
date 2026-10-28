class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        block = defaultdict(set)
        for i in range(9) :
            for j in range(9) :
                b = board[i][j]
                if b == "." :
                    continue
                # row
                if b in row[i] :
                    return False
                row[i].add(b)
                # col
                if b in col[j] :
                    return False
                col[j].add(b)
                # block
                key = (i // 3, j // 3)
                if b in block[key] :
                    return False
                block[key].add(b)
        return True
        