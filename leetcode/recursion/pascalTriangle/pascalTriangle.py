import functools

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        num_cols = rowIndex + 1
        ans = []
        
        for j in range(0, num_cols):
            print(j)
            ele = pascalTriangle(rowIndex, j)
            ans.append(ele)
        return ans

@functools.cache
def pascalTriangle(rowi: int, colj: int) -> int:
    if (colj == 0 or rowi == colj):
        return 1
    else:
        # left = pascalTriangle(rowi - 1, colj - 1)
        # right = pascalTriangle(rowi - 1, colj)
        # print('left: ', left, 'right: ', right)
        # return left + right   
        return pascalTriangle(rowi - 1, colj - 1) + pascalTriangle(rowi - 1, colj)