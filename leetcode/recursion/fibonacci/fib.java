import java.util.HashMap;

class Solution {
    HashMap<Integer, Integer> cache = new HashMap<Integer, Integer>();
    
    public int fib(int n) {
        if (cache.containsKey(n)) {
            return cache.get(n);
        }
        int ans;
        
        if (n <= 1) {
            ans = n;
        } else {
            ans = fib(n-1) + fib(n-2);
        }
        cache.put(n, ans);
        return ans;
        
    }
}