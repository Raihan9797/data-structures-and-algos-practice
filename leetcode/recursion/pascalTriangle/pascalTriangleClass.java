import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class pascalTriangleClass {
    public static int[][] memo = new int[500][500];


    public List<Integer> getRow(int rowIndex) {

        int num_cols = rowIndex + 1;
        LinkedList<Integer> ans = new LinkedList<Integer>();
        
        for (int j = 0; j < num_cols; j++) {
            // System.out.println(j);

            int ele = memoPascalTriangle(rowIndex, j);
            // System.out.println(ele);
            ans.add(ele);
        }
        return ans;
    }
    
    /*
    MEMOIZED RECURSIVE VERSION
    */
    public static int memoPascalTriangle(int rowi, int colj) {
        // System.out.println("running");
        System.out.println(memo[rowi][colj]);
        if (colj == 0 || colj == rowi) {
            memo[rowi][colj] = 1;
            return 1;
        } else if (memo[rowi][colj] != 0) {
            System.out.println("memoing");
            return memo[rowi][colj];
            
        } else {
            int left = memoPascalTriangle(rowi - 1, colj - 1);
            int right = memoPascalTriangle(rowi - 1, colj);
            // print('left: ', left, 'right: ', right)
            System.out.println("saving");
            memo[rowi][colj] = left + right;
            return memo[rowi][colj];
            // return left + right;    
            // return memoPascalTriangle(rowi - 1, colj - 1) + memoPascalTriangle(rowi - 1, colj);
        }
    }

    /*
    THIS IS THE RECURSIVE VERSION
    */
    public static int pascalTriangle(int rowi, int colj) {
        // System.out.println("running");
        if (colj == 0 || colj == rowi) {
            return 1;
        } else {
            // int left = pascalTriangle(rowi - 1, colj - 1);
            // int right = pascalTriangle(rowi - 1, colj);
            // print('left: ', left, 'right: ', right)
            // return left + right;    
            return pascalTriangle(rowi - 1, colj - 1) + pascalTriangle(rowi - 1, colj);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int rowi = sc.nextInt();
        sc.close();
        pascalTriangleClass ptc = new pascalTriangleClass();
        List<Integer> ans = ptc.getRow(rowi);
        System.out.println(ans);



    }

}