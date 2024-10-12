class Solution {
    static int N = 0;
    static int answer = 0;
    public int solution(int[] numbers, int target) {
        N = numbers.length;
        
        dfs(0, -1*numbers[0], target, numbers);
        dfs(0, numbers[0], target, numbers);
        
        return answer;
    }
    
    public void dfs(int idx, int result, int target, int[] numbers) {
        if (idx == N-1 && result == target) {
            answer++;
            return;
        }
        if (idx >= N-1) {
            return;
        }
        if (idx + 1 < N) {
            dfs(idx+1, result+numbers[idx+1], target, numbers);
            dfs(idx+1, result-numbers[idx+1], target, numbers);
        }
    }
}