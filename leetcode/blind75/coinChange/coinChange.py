class Solution:
    def find_valid(self, counts):
        """
        given a list of counts:
        find the smallest valid count (ie not -1)
        else return -1
        """
        smallest = 9999999
        for c in counts:
            if c == -1:
                continue
            if c < smallest:
                smallest = c
        if smallest == 9999999:
            smallest = -1
        return smallest
       

    def helper(self, count: int, coins: List[int], amount: int) -> int:
        if amount < 0:
            return -1
        elif amount == 0:
            return count
        else:
            counts = []
            for coin in coins:
                cnt = self.helper(count+1, coins, amount-coin)
                counts.append(cnt)
            #print(counts)
            return self.find_valid(counts)
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        # return self.helper(0, coins, amount)
        
        ### initialize the array to be full of the amount + 1
        ### cos even when using just a $1 coin, it can never be more than amt itself.
        dp = [amount + 1] * (amount + 1)
        ### base case: amount of 0 means no action req
        dp[0] = 0

        ### for each element in arr (starting from the smallest)
        ### basically doing a smaller amount a and building up our dp array
        for a in range(1, len(dp)):
            ### loop through each coin and find the diff
            for c in coins:
                diff = a - c
                #print(diff)

                ### if diff is valid ie not < 0
                if diff >= 0:
                    #print(dp[i], 1+dp[diff])
                    ### find the minimum action
                    ### whatever you have now vs the new diff + 1 action
                    dp[a] = min(dp[a], 1 + dp[diff])
                else:
                    continue
        ### get the solution for the amount
        soln = dp[amount]
        #print(dp)

        ### if the solution didnt change, there is no actual solution
        if soln == amount + 1:
            ### so return -1
            soln = -1
        return soln
                
        