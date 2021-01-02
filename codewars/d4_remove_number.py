# Problem: Is my friend cheating - https://www.codewars.com/kata/5547cc7dcad755e480000004
# Given n, n > 0
# from a sequence of 1 to n he chooses 2 numbers, a and b
# the sum of all the numbers excluding a and b == a * b
# can you find all the possible (a,b) pairs?


# Examples
# notice that the solutions are sorted by increasing a
# remov_nb(100) -> []
# remov_nb(26)-> [(15, 21), (21, 15)]



''' What i learned
## Technical ##
1. checking whether an element x is an integer
- method a:
x - int(x) == 0.0

- method b:
x.is_integer()

2. My answer is basically the same as the better solution, with a few minor mistakes that was not checked
- b <= n. as b could be the n itself!

3. ** When you need to find to multiple values, make sure to move all the values to one side!!
- it sounds obvious, especially if you write it down and do it like a math question, but it seems to evade you when coding!
- because you want b:
- b = (total_sum - a) / (a + 1)


## Non-technical ##
1. Writing down these problem, especially in the form of equations really helps. 

'''


## My Solution ##
def remov_nb(n):
    total_sum = (n+1) * (n/2) # arithmetic progression
    
    solutions = []
    for a in range(1, n+1):
        b = (total_sum - a) / (a + 1) # move b to one side of the equation
        if (b < n and b - int(b) == 0): 
            # b needs to be within 1 to n and it needs to be a whole number!
            solutions.append((a, int(b)))
    # print(solutions)
    return solutions

## Better Solution ##
def remov_nb_better(n):
    total = (n+1)*(n/2)

    solutions = []
    for a in range(1, n+1):
        b = (total - a)/(a+1)
        if b.is_integer() and b <= n:
            solutions.append((a, int(b)))
    return solutions


## Testing ##
total_sum = 0
n = 26
for i in range(1, n+1):
    total_sum += i
total_sum # 3 -> 6, 4 -> 10

int((3 + 1) * (3/2))
int((4 + 1) * (4/2))
int((5 + 1) * (5/2))
