# Last updated: 6/11/2025, 3:38:36 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = {}

        for i in strs:
            sortedWord = ''.join(sorted(i)) 
            if sortedWord not in wordMap:
                wordMap[sortedWord] = []
            wordMap[sortedWord].append(i)
            
        return list(wordMap.values())

