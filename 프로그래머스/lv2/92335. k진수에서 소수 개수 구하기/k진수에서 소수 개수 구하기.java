import java.util.*;
class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        StringBuilder sb = new StringBuilder("");
        
        while(true){
            sb.append(n % k);
            n = n / k;
            if(n < k){
                sb.append(n);
                break;
            }
        }
        String num = sb.reverse().toString();
        //String[] each = num.split("0");
        StringTokenizer st = new StringTokenizer(num, "0");
        while(st.hasMoreElements()){
            long knum = Long.parseLong(st.nextToken());
            if(knum == 1)
                continue;
            if(knum == 2){
                answer++;
                continue;
            }
            if(isPrime(knum))
                answer++;
        }
        return answer;
    }
    
    public boolean isPrime(long knum){
        for(int i = 2; i <= (int)Math.sqrt(knum); i++){
            if(knum % i == 0)
                return false;
        }
        return true;
    }
}