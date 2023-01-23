class Solution {
    
    int answer = 0;
    int sum = 0;
    public int solution(int[] nums) {

        for(int i = 0; i < nums.length-2; i++){
            for(int j = i+1; j < nums.length-1; j++){
                for(int z = j+1; z < nums.length; z++){
                    sum = nums[i] + nums[j] + nums[z];
                    if(isPrime(sum)) answer++;
                }
            }
        }
        return answer;
    }
    
    public boolean isPrime(int sum){
        for(int k = 2; k < sum ; k++){
            if(sum % k == 0)
                return false;
        }
        return true;
    }
}