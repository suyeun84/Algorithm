import java.util.*;
class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        HashMap<String, Integer> hashmap = new HashMap<>();
        int cnt = 0;
        for (int i = 0; i < number.length; i++) {
            cnt += number[i];
        }
        if (cnt > discount.length) return answer;
        //슬라이딩 윈도우
        for (int i = 0; i < discount.length; i++) {
            hashmap.put(discount[i], hashmap.getOrDefault(discount[i], 0)+1);
            if (i < cnt-1) continue;
            else if (i > cnt-1) {
                hashmap.replace(discount[i-cnt], hashmap.getOrDefault(discount[i-cnt], 0)-1);                
            }
            // 갯수 확인
            boolean flag = true;
            for (int j = 0; j < want.length; j++) {
                if (hashmap.getOrDefault(want[j], 0) != number[j]) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                answer += 1;
            }
        }
        return answer;
    }
}