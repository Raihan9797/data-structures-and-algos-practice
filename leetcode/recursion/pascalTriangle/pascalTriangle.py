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

    # ITERATIVE VERSION
    def iterGetRows(rowi: int):
        # start with row 0
        ans = []
        ans.append(1)
    
        # keep making new rows and replacing them
        # row 0 : [1] (already made)
        # row 1 : [1, 1]
        # row 2 : [1, 2, 1]
        # row 3 : [1, 3, 3, 1]
        # so to get row 3 from 1,
        # we need 1, 2, 3 increaments thus rowi + 1
        for i in range(1, rowi+1):
            new_row = []
            
            # row 3 has 4 ele: [1, 3, 3, 1]
            # indexes:         [0, 1, 2, 3]
            for j in range(0, i + 1):
                ele = 0
                # base cases are 1
                if (j==0 or j==i):
                    ele = 1
                else:
                    left = ans[j-1]
                    right = ans[j]
                    ele = left + right
    
                new_row.append(ele)
            ans = new_row
        return ans


# CACHED RECURSIVE VERSION
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
