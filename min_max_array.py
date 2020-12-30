# min max arrays takes an unsorted array and returns an array such that the first element is the biggest element followed by the smallest, followed by the second biggest and then second smallest etc..
# link: https://www.codewars.com/kata/5a090c4e697598d0b9000004

# input:[15,11,10,7,12]
# output:[15,7,12,10,11]

# input:[1,6,9,4,3,7,8,2]
# output:[9,1,8,2,7,3,6,4]

""" 
What i leared from this problem 

## technical aspects ##
1. basic refresher of things like arr.sort() vs sorted(arr)

2. ternary operators in python
end = int(length / 2) if is_even else int(length / 2 + 1)

3. the better solution makes use of the already available python function, pop() which removes elements at the end of the list VS you using indexes to remove the elements

4. Using pop() on the original list means we no longer have to keep track of the list for out of bounds errors!

5. The length of the list being even or odd mattered in this case.


## non technical aspects ##
1. It really helps to run through the program on paper first

2. Work through the problems which you have errors. This usually occurs around VARIABLES which you think you know how they work, but you don't.
"""

## Your Solution ##
def solve(arr):
    sorted_arr = sorted(arr) # [7,10,11,12,15]
    length = len(arr) # 5
    is_even = length % 2 == 0
    end = int(length / 2) if is_even else int(length /2 +1)
    ans = []
    
    for i in range(0, end):
        if (i == end-1 and not is_even):
            ans.append(sorted_arr[i])
            break
        ans.append(sorted_arr[length-i-1])
        ans.append(sorted_arr[i])
    return ans




## A better solution ##
def solve(arr):
    arr = sorted(arr)
    res = []
    while len(arr):
        res.append(arr.pop())
        if len(arr):
            res.append(arr.pop(0))
    return res


arr1 = [15,11,10,7,12]
solve(arr1)
# output:[15,7,12,10,11]

arr2 = [1,6,9,4,3,7,8,2]
solve(arr2)
# output:[9,1,8,2,7,3,6,4]