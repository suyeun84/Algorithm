import java.util.Scanner;

public class Main {

    public static int max(int a, int b){
        if(a>b)
            return a;
        else
            return b;
    }

    public static void main(String[] args){
        Scanner scanner= new Scanner(System.in);

        int size= scanner.nextInt();
        int a=0;
        int triangle[][]=new int[size][size];
        int dp[][]=new int[size][size];

        for(int i=0; i<size; i++){
            for(int j=0; j<=i; j++){
                triangle[i][j]=scanner.nextInt();
            }
        }
        dp[0][0]=triangle[0][0];

        for(int i=1; i<size; i++){
            dp[i][0]=dp[i-1][0]+triangle[i][0];
            dp[i][i]=dp[i-1][i-1]+triangle[i][i];

            for(int j=1; j<i; j++){
                dp[i][j]=max(dp[i-1][j-1]+triangle[i][j], dp[i-1][j]+triangle[i][j]);
            }//입력완료
        }
        int result=0;
        for(int i=0; i<size; i++){
            if(dp[size-1][i]>result){
                result=dp[size-1][i];
            }
        }
        System.out.println(result);
    }
}
