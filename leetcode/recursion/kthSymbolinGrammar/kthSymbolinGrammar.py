class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def switch(val: int) -> int:
            if val == 0:
                return 1
            else:
                return 0
        
        if n == 1 and k == 1:
            return 0
        else:
            # if even, switch
            prev_k = k - int(k/2)
            if k % 2 == 0:
                return switch(self.kthGrammar(n-1, prev_k))
            
            # if odd, dont switch
            else:
                return self.kthGrammar(n-1, prev_k)