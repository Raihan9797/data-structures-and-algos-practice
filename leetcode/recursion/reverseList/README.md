# Link
https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/3233/

## Insight
1. How wishful thinking is "connected": you thought that the tail reverse would look smth like
```
head-> 1 -> 2 -> 3 -> null

head-> 1 -> 3 -> 2 -> null

In reality, its actually:
head-> 1 -> 2 <- 3 <- newhead
            |
            null (hard to display this on markdown)

Then complete the reversal:
null <- 1 <- 2 <- 3 <- newhead
```

Which is why you couldnt solve the question initially.