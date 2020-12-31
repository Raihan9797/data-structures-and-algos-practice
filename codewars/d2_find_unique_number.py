# problem: Array with some numbers
# - ALL NUMBERS ARE EQUAL except 1
# - Array contains at least 3 numbers
# = test contain very huge arrays so think about performance.

# Examples
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) -> 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) -> 0.55

''' What I learned
# technical #
1. better solution: multiple assignments in one line!

2. slicing arrays does not include the ending number
- arr[:3] only gives element 0,1,2!

3. ONLY ADDING CONDITIONS THAT ACTUALLY CHANGE MY SOLUTIONS. This can only be seen by running through the special cases

4. i already knew about sets, was just trying to see how to do it without it



# Non-technical #
1. You can actually continue to improve upon your code by running through on paper
- you realised that your for loop keeps reassigning the number! so just reassign once and BREAK!

2. You still keep making simple assumptions: it's much better to run through the code slower instead of thinking you know how exactly it runs!

'''

## my solution ##
def find_uniq(arr):
    first, second, third = arr[:3]
    
    for number in arr: # detect diff numbers
        if first != number:
            ans = number
            break
    

    if first != second: 
        # ie either 1st or 2nd is unique!
        # ans is currently second -> no need to reassign if its correct!
        if first != third:
            # this means first is the unique ele -> reassign
            ans = first
        # else do nothing; second is the correct ans!
        
    return ans


## better solution ##
def find_uniq(arr):
    a, b = set(arr)
    return a if arr[:2].count(a) == 1 else b


## testing ##
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) -> 2
arr1 = [1, 1, 1, 2, 1, 1]
find_uniq(arr1)
# find_uniq([ 0, 0, 0.55, 0, 0 ]) -> 0.55