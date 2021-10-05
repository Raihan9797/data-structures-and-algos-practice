class Solution:
    def myPow(self, x: float, n: int) -> float:

        ############################################
        ### OPTIMAL SOLUTION
        ############################################
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            positive_n = -1 * n
            reciprocal_x = 1/x
            return self.myPow(reciprocal_x, positive_n)
        else:
            if (n % 2 == 0) :
                half = self.myPow(x, int(n/2))
                return half * half
            else:
                return x * self.myPow(x, n - 1)
        
        ############################################
        ### NAIVE NON TAIL RECURSIVE RECURSIVE SOLUTION ###
        ############################################
        # if n == 0:
        #     return 1
        # elif n == 1:
        #     return x
        # elif n < 0:
        #     positive_n = -1 * n
        #     reciprocal_x = 1/x
        #     return self.myPow( reciprocal_x, positive_n)
        # else:
        #     return x * self.myPow(x, n - 1)  


        ############################################
        ### NAIVE TAIL RECURSIVE SOLUTION ###
        ############################################
        # def helper(x: float, n: int, acc: float) -> float:
        #     if n == 0:
        #         return 1
        #     elif n == 1:
        #         return acc * x
        #     elif n < 0:
        #         positive_n = -1 * n
        #         reciprocal_x = 1/x
        #         return helper(reciprocal_x, positive_n, acc)
        #     else:
        #         return helper(x, n-1, acc*x)
        # return helper(x, n, 1.0)

        ############################################
        ### NAIVE ITERATIVE SOLUTION: STILL TLE! ###
        ############################################
        # acc = 1.0
        # if n < 0:
        #     new_x = 1/x
        #     new_n = -n
        #     for i in range(0, new_n):
        #         acc *= new_x
                
        # else:
        #     for i in range(0, n):
        #         acc *= x
        # return acc