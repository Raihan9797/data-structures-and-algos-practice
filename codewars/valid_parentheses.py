# Problem: a fn that takes in a string of and determines if the parentheses is valid.

# Examples: 
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# "(zzkvejfsh)iq    =>  true


""" What I learned
## technical ##
1. Python does NOT have a stack implementation!
- pop() by default removes the LAST element
- does NOT have a push(): use insert(0, element) instead!

2. The 'better' solution is more efficient as it uses a counter instead of making a list. But the idea of popping and pushing into a stack is the same!

3. However, my method can incorporate other brackets by making sure the top of the stack matches the bracket to be removed!!

## non technical ##
"""


## My solution ##
def valid_parentheses(string):
    if (string == ""): return True # if empty, vacuosly True
    else:
        stack = []
        for char in string: # iterate through the chars
            if char == "(": # if ( , push it into the stack
                stack.insert(0, char)
            elif char == ")" and stack: # if ) and there is a (, remove it
                stack.pop(0)
            elif char == ")" and not stack: # if ) and there is NO (, it's invalid
                return False
            # other chars are skipped
            
        if stack: return False # if there are remaining (, its invalid
        else: return True # else its valid!


## Better solution ##
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False
