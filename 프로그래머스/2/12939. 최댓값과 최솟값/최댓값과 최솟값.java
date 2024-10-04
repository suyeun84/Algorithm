class Solution {
    public String solution(String s) {
        String answer = "";
        String[] num = s.split(" ");
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        for(int i = 0; i < num.length; i++){
            int number = Integer.parseInt(num[i]);
            max = Math.max(max, number);
            min = Math.min(min, number);
        }
        answer = min+" "+max;
        return answer;
    }
}