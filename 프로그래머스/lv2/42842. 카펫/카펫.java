class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        int total = brown + yellow;
        for(double width = Math.ceil(Math.sqrt(total)); width < brown; width++){
            int height;
            if(total % width == 0){
                height = total / (int)width;
            }else
                continue;
            if(width*2+height*2-4 == brown){
                answer[0] = (int)width;
                answer[1] = height;
                break;
            }
        }
        return answer;
    }
}