class Solution {
    public double myPow(double x, int n) {
        double acc = 0.0;
        if (n < 0) {
            return myPow(1/x, -1 * n);
        } else if (n == 0) {
            return 1;
        } else if (n == 1) {
            return x;
        } else {
            if (n % 2 == 0) {
                double half = myPow(x, (int) (n / 2));
                return half * half;
            } else {
                return x * myPow(x, n - 1);
            }
        }
        
    }
}