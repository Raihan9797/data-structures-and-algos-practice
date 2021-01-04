# Problem: hashtag generator - https://www.codewars.com/kata/52449b062fb80683ec000024

# simple hashtag generator
# - all words must have first letter capitalized
# if final result is longer than 140 chars -> return False
# if input is '' -> return False


# Examples
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"

# "    Hello     World   "   =>  "#HelloWorld"

# ""   =>  false



''' What i learned
## Technical ##
1. Not much but i revised strings. capitalize() to get first word capitalized
- upper() for all UPPER CASE
- lower() for all lower case

2. The better solution is just much more compact and still easily understandable

## Non-technical ##

'''

## My Solution ##
def generate_hashtag(s):
    # strip, split and capitalize words
    words = s.strip().split(' ')
    cap_words = [word.capitalize() for word in words]
    # print(cap_words)
    
    # join the words
    joined = ''.join(cap_words)
    print(len(joined))
    
    # False cases
    if (joined == '' or len(joined) >= 139): return False
    
    # True cases
    return '#' + ''.join(cap_words)


## Better Solution ##
def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output


## Testing ##