import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 1;
        while(n != 1){
            if(n % 2 == 0)
                n = n/2;
            else{
                answer++;
                n -= 1;
            }
        }
        return answer;
    }
}