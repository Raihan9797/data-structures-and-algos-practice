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

def iterPascalTriangle(rowi: int, colj: int) -> int:
    if (colj == 0 or rowi == colj):
        return 1
    else:
        for i in range(0, rowi):
            for j in range(0, colj):
                print(i)


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
