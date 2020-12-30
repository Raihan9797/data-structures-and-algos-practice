## problem: morse code decoder. A dictionary of MORSE_CODE has been given to you which has:
# keys ('....')
# values ('H')
# special Keys ('...---...') : ('SOS')
# for coding purposes, use ASCII characters not Unicode (doesn't really affect your code)

# input: ".... . -.--   .--- ..- -.. ."

# output: "HEY JUDE"

"""
What i leared
## technical ##
1. The main issue was handling white spaces. Splitting resulted in 2 ''s which i had to process as a ' ' for the ans
- split helps to remove unecessary white spaces, but only if you know how to process it after

2. making use of ans += instead of appending my ans to a different list, which was not efficient

3. using enumerate(code) to get an index to "look ahead" helped in this question!

4. The better solution preprocesses the code by looking for '   ' which is essentially the space between WORDS, while ' ' is the space between CHARACTERS

## non-technical ##
1. Your paper answer supposedly helped, but created an issue of not saving the last letter. It's ok to go back to your old code instead!

"""

## my solution ##
def decodeMorse(morse_code):
    print(morse_code)
    mc = morse_code.strip() # strip empty spaces on both sides
    # print(mc)
    letters = mc.split(' ') # split by blank space
    # print(letters)
    ans = ''
    for idx, l in enumerate(letters): # iterate through coded letters
        if l == '': # if empty string
            if letters[idx+1] == '': # include a blank space
                ans += ' '
            else: # already included blank space once, so skip it!
                continue
        else: # decode the letter and add it to ans
            ans += MORSE_CODE[l]
    print(ans)
    return ans


## better solution ##
def decodeMorse(morseCode):

    morseCode = morseCode.strip().replace("   ", " * ") # convert the word spacing to something that only has to be traversed once!!

    msg = ""
    
    for x in morseCode.split():
        if x != "*":
            msg += MORSE_CODE[x]
        else:
            msg += " "
    
    return msg