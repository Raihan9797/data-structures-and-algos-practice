### link
https://leetcode.com/problems/coin-change/submissions/

### problem
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

### my understanding of the solution
Dynamic programming question. Start from bottom up.

    1. initialize memo array. Each index represents and amount and the value is the minimum amount of coins required.
    2. initialize the values to be amount + 1
    3. base case: when amount = 0: no actions / coins required.
    4. recursive case: 
        * for each smaller amount in the memo
            - loop through all coins and minus off
            - if the result is valid, compare this new action + the value of the difference with the current value of this amount. the smaller one is the new value for the amount
    5. return the value for the amount we actually want to find.
    6. if the value has not changed from the initial value, it means there are no valid values. So return -1


### insights
1. Doing the slow recursive methods brings up a lot of issues. For a first try, it's not bad. But it's not as easy as I thought. For one thing, the fact that invalid case is -1 means I can't use min to find the smallest amount that I already computed. So needed to create a find_valid().

2. dp method was found on youtube. the most confusing part was starting from the bottom up. When I tried to implement without looking at the solution, i used the actual amount instead of the smaller amounts, which is what we are building up to.
- The part where this new smaller amount is subtracted from the coin is what confused me. We do this because i. we want to check if the subtracted value is valid for us to continue building upon. 
- If the subtracted value is valid, we actually go and look at the memoized value for this new subtracted value so we just + 1 to it.
- So we need to compare the current memoized value with this new value ie. `dp[a] = min(dp[a], 1 + dp[a-c])
