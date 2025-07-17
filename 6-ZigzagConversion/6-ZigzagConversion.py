# Last updated: 7/17/2025, 6:50:37 PM
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        strings = [''] * numRows
        # [0, 1, 2]
        count = 0
        flag = True
        
        for c in s:
            strings[count] += c
            
            if flag:
                count += 1
            elif not flag:
                count -= 1
                
            if count == numRows - 1:
                flag = False
            elif count == 0:
                flag = True
                
        res = ''.join(strings)
        return res