import java.util.*;
class Solution {
    public int solution(String dirs) {
        HashSet<String> answer = new HashSet<>();
        int y = 0, x = 0;
        for (char dir: dirs.toCharArray()) {
            int ny = y, nx = x;
            if (dir == 'U') {
                ny += 1;
            } else if (dir == 'D') {
                ny -= 1;
            } else if (dir == 'L') {
                nx -= 1;
            } else {
                nx += 1;
            }
            if (Math.abs(ny) > 5 || Math.abs(nx) > 5) continue;
            answer.add(y+","+x+","+ny+","+nx);
            answer.add(ny+","+nx+","+y+","+x);
            y = ny;
            x = nx;
        }
        return answer.size() / 2;
    }
}