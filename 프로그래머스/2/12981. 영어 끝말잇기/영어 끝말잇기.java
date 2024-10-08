import java.util.*;
class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        HashMap<String, Integer> hm = new HashMap<>();
        hm.put(words[0], 1);
        for (int i = 1; i < words.length; i++) {
            if (hm.containsKey(words[i]) || (words[i-1].charAt(words[i-1].length()-1) != words[i].charAt(0))) {
                answer[0] = i % n + 1;
                answer[1] = i / n + 1;
                break;
            }
            hm.put(words[i], 1);
        }
        
        return answer;
    }
}