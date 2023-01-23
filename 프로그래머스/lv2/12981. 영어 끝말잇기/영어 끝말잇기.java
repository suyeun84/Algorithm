import java.util.*;
class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        HashMap<String, Integer> hashmap = new HashMap<>();
        
        String prev = words[0];
        hashmap.put(words[0], 0);
        for(int i = 1; i < words.length; i++){
            if(prev.charAt(prev.length()-1) != words[i].charAt(0)){
                answer[0] = i % n + 1;
                answer[1] = i / n + 1;
                return answer;
            }
            if(hashmap.containsKey(words[i])){
                answer[0] = i % n + 1;
                answer[1] = i / n + 1;
                return answer;
            }
            hashmap.put(words[i], 0);
            prev = words[i];
        }
        return answer;
    }
}