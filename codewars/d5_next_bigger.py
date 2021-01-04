# Problem: Next Bigger - https://www.codewars.com/kata/55983863da40caa2c900004e
# Create a function that takes a positive integer and returns the NEXT BIGGER NUMBER that can be formed by rearranging its digits.
# - if digits can't be rearranged to form a bigger number, return -1 


# Examples
# 12 --> 21
# 513 - > 531
# 2017 - 2071

# 9 -> -1
# 111 -> -1
# 531 -> -1

#** 6938652 -> 6952368



''' What i learned
## Technical ##
1. Reminder of how to reverse a list:
- reversed_list = my_list[::-1]

2. inserting from the front:
- my_list.insert(0, element)

3. Getting a list of chars from a string
- chars = list(my_string)

4. Checking whether the numbers are the same
eg. num = 111
len(set(list(str(num)))) # returns 1 if all numbers are the same!

5. Making use of flags: If you have too many, it might not be the right way
is_swapped = False
if (not is_swapped and ...)
is_swapped = True

6. list_num -> list_char -> one_string:
## join a list of int into a big int
int_list = [1, 2, 3]
char_list = [str(x) for x in int_list]
s = ''
ans = int(s.join(char_list))
ans

7. Find the smallest number that is bigger than a certain number, t[0]. use MIN()!!
t = [3, 8, 6, 5, 2] # we are trying to get 5
m = min(filter(lambda x: x>t[0], t)) # find the smallest number that is bigger than your problematic number


## Non-technical ##
1. Only when you try out a question do you realise the edge cases. Initially, you thought the problem was just about swapping the last 2 digits
Then it became swapping 2 digits from front to back
Then it became looking out for cases where the last char was a 0

2. The problem got more complex, beyond being able to complete it within a day. So you looked for an algorithm to solve this issue after being told that it existed through the comments
- don't copy, understand what is going on and then implement it yourself
- Useful link: https://www.ideserve.co.in/learn/next-greater-number-using-same-digits#:~:text=For%20example%2C%20if%20the%20given,should%20return%20the%20same%20number.


'''

## My Solution ##
def next_bigger(n):
    '''
    6938652 -> 6958632 -> 6952368
    1. check from the right: next > current
    if true, store in array
    else: note the number (3 NOT > 8)
    and note the index, i

    2. swap with the next biggest number on the right side.
    = in this case 5
    6958632

    3. sort from i + 1
    '''
    string = str(n)
    length = len(string)
    digits = [int(char) for char in string]
    rhs = []
    index = None
    reversed_digits = digits[::-1]
    for idx, curr in enumerate(reversed_digits[:-1]):
        nextt = reversed_digits[idx+1]
        # print(nextt, curr)
        if (nextt < curr):
            rhs.insert(0, curr)
            index = idx + 1
            break
        else:
            rhs.insert(0, curr)
    print(rhs)

    if index == None: return -1

    # swap with next biggest number on rhs
    swapper = reversed_digits[index]
    new_rhs = sorted(rhs)
    temp = None
    for idx, num in enumerate(new_rhs):
        if swapper < num:
            temp = num
            new_rhs[idx] = swapper
            break
    new_rhs.insert(0, temp)
    for d in reversed_digits[index+1:]:
        new_rhs.insert(0, d)
    
    # print(new_rhs, temp)
    # print(digits)
    # print(reversed_digits[index+1:])
    # print(index)
    
    char_ans = [str(x) for x in new_rhs]
    ans = int(''.join(char_ans))
    return ans


## Better Solution ##
def next_bigger(n):
    s = list(str(n)) # convert to chars_list
    for i in range(len(s)-2,-1,-1): # iterate from the back
        # len(s) -2 so you can look forward at the last element without any errors
        if s[i] < s[i+1]:
            t = s[i:] # copy the right side of the numbers
            m = min(filter(lambda x: x>t[0], t)) # find the smallest number that is bigger than your problematic number
            t.remove(m) 
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1


## Testing ##
next_bigger(2017)
next_bigger(6938652)
next_bigger(31)

