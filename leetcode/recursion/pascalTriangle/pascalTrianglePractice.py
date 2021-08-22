from typing import List
import functools

@functools.cache
def pascalTriangle(rowi: int, colj: int) -> int:
    # print("running")
    if (colj == 0 or rowi == colj):
        return 1
    else:
        left = pascalTriangle(rowi - 1, colj - 1)
        right = pascalTriangle(rowi - 1, colj)
        # print('left: ', left, 'right: ', right)
        return left + right


# print(pascalTriangle(0, 0))
# 
# print(pascalTriangle(1, 0), pascalTriangle(1, 1))
# 
# print(pascalTriangle(2, 0), pascalTriangle(2, 1), pascalTriangle(2, 2))
# 
# print(pascalTriangle(3, 0), pascalTriangle(3, 1), pascalTriangle(3, 2), pascalTriangle(3, 3))
# 
# print(pascalTriangle(4, 0), pascalTriangle(4, 1), pascalTriangle(4, 2), pascalTriangle(4, 3), pascalTriangle(4, 4))
# 
# print(pascalTriangle(5, 0), pascalTriangle(5, 1), pascalTriangle(5, 2), pascalTriangle(5, 3), pascalTriangle(5, 4), pascalTriangle(5, 5))


def getRow(rowIndex: int) -> List[int]:
    num_cols = rowIndex + 1
    ans = []
    
    for j in range(0, num_cols):
        # print(j)
        ele = pascalTriangle(rowIndex, j)
        ans.append(ele)
    return ans

# print(getRow(25))

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


def memoPascalTriangle(rowi: int, colj: int) -> int:
    # print("running")
    memo = [[-1]*1_000_000]*1_000_000

    if (colj == 0 or rowi == colj):
        return 1
    elif (memo[rowi][colj] == None): 
        return memo[rowi][colj]
    else:
        left = memoPascalTriangle(rowi - 1, colj - 1)
        right = memoPascalTriangle(rowi - 1, colj)
        # print('left: ', left, 'right: ', right)
        memo[rowi][colj] = left + right
        return left + right

def memoHelp(rowi: int, colj: int) -> int:


print('SPEED TESTT')
# print(memoPascalTriangle(50, 3))
print(pascalTriangle(150, 3))
