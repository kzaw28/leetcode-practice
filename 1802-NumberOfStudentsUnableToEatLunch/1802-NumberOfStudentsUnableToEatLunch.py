# Last updated: 5/27/2025, 6:45:52 PM
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        # Returns a map that counts number of values for each unique key
        countMap = Counter(students)

        # Check each sandwich if there is people in countMap left that wants it
        for sandwich in sandwiches:
            if countMap[sandwich] > 0:
                res -= 1
                countMap[sandwich] -= 1
            else:
                return res

        return res