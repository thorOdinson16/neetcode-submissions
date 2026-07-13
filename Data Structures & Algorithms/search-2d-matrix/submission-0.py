class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flag = False
        for i in matrix:
            x = set(i)
            if target in x:
                flag = True
                break
        return flag