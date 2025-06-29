# Last updated: 6/28/2025, 11:35:24 PM
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(boxGrid), len(boxGrid[0])

        for r in range(ROWS):
            # Pointer for next available space
            i = COLS - 1 # last pos for the next available space
            for c in reversed(range(COLS)):
                # if its a stone, we can swap with the next available
                # space (i)
                if boxGrid[r][c] == "#":
                    boxGrid[r][c], boxGrid[r][i] = boxGrid[r][i], boxGrid[r][c]
                    i -= 1 
                if boxGrid[r][c] == "*":
                    i = c - 1
        res = []
        for c in range(COLS):
            col = []
            for r in reversed(range(ROWS)):
                col.append(boxGrid[r][c])
            res.append(col)
        return res