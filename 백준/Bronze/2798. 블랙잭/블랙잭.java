import java.util.Scanner;

public class Main {

    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);
        int n,m;
        int sum=0;
        n=scanner.nextInt(); // n장
        m= scanner.nextInt(); //m 넘지 않게
        int card[]= new int[n];

        for(int i=0; i<n; i++){
            card[i]= scanner.nextInt();
        }
        
        int result=0;
        Label:
        for(int i=0; i<n-2; i++){
            for(int j=i+1; j<n-1; j++){
                for(int h=j+1; h<n; h++){
                    sum=card[i]+card[j]+card[h];
                    if(m == sum){
                        result=m;
                        break Label;
                    }
                    if(sum<m && sum>result){
                        result=sum;
                    }
                }
            }
        }
        System.out.println(result);
    }
}