class Solution {
    HashMap<Integer, Integer> cache = new HashMap<Integer, Integer>();

    public int climbStairs(int n) {
        if (cache.containsKey(n)) {
            return cache.get(n);
        }
        
        int ans;
        if (n < 0) {
            ans = 0;
        } else if (n == 0) {
            ans = 1;
        } else {
            ans = climbStairs(n-1) + climbStairs(n-2);
        }
        
        cache.put(n, ans);
        return ans;
        
    }
}