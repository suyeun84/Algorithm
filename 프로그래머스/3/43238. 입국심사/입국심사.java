import java.util.*;
class Solution {
    public long solution(int n, int[] times) {
        Arrays.sort(times);
        long answer = Long.MAX_VALUE;
        long start = 0;
        long end = (long)times[times.length-1]*(long)n;
        while (start <= end) {
            long mid = (start + end) / 2;
            long total = 0;
            for (int i = 0; i < times.length; i++) {
                total += mid / times[i];
            }
            if (total < n) {
                start = mid + 1;
            } else {
                answer = Math.min(answer, mid);
                end = mid - 1;
            }
        }
        return answer;
    }
}