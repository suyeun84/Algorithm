import java.util.*;
class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        
        HashMap<Character, Integer> hashmap = new HashMap<>();
        for(int i = 0; i < skill.length(); i++){
            hashmap.put(skill.charAt(i), i);
        }
        
        for(int i = 0; i < skill_trees.length; i++){
            char[] skills = skill_trees[i].toCharArray();
            int a = 0;
            boolean flag = true;
            for(int j = 0; j < skills.length; j++){
                char curr = skills[j];
                if(hashmap.containsKey(curr)){
                    if(hashmap.get(curr) != a){
                        flag = false;
                        break;
                    }else
                        a++;
                }
            }
            if(flag)
                answer++;
        }
        return answer;
    }
}