# Last updated: 7/17/2025, 7:23:46 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        
        if len(words) == 1:
            return words[0]
        
        res = ''
        for i in range(len(words)- 1, -1, -1):
            res += words[i]
            if i != 0:
                res += ' '
    
        return res