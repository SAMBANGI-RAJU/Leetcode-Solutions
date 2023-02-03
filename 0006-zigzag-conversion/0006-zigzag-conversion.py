class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        rows = [""] * numRows
        x,y = 0,0
        delta = (1,0)

        for c in s:
            rows[x] += c

            # adapt delta
            if x+1 == numRows:
                delta = (-1,1)
            elif x == 0:
                delta = (1,0)

            x, y = x+delta[0], y+delta[1]

        return "".join(rows)