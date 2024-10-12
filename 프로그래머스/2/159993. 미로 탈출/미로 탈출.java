import java.util.*;
class Solution {
    int ry = 0, rx = 0, sy = 0, sx = 0, N = 0, M = 0;
    public int solution(String[] maps) {
        int answer = 0;
        // 레버의 위치 파악
        N = maps.length;
        M = maps[0].length();
        String[][] map = new String[N][M];
        for (int i = 0; i < maps.length; i++) {
            for (int j = 0; j < maps[i].length(); j++) {
                map[i][j] = String.valueOf(maps[i].charAt(j));
                if (map[i][j].equals("L")) {
                    ry = i;
                    rx = j;
                } else if (map[i][j].equals("S")) {
                    sy = i;
                    sx = j;
                } 
            }
        }
        // S -> 레버
        int res = bfs(sy, sx, map, "L");
        if (res == -1) {
            return -1;
        }
        answer += res;
        // 레버 -> E
        res = bfs(ry, rx, map, "E");
        if (res == -1) {
            return -1;
        }
        answer += res;
        return answer;
    }
    
    public int bfs(int y, int x, String[][] map, String target) {
        int[][] d = new int[][]{{1,0},{-1,0},{0,1},{0,-1}};
        Queue<int[]> q = new LinkedList<>();
        int[][] visited = new int[N][M];
        for (int[] v: visited) {
            Arrays.fill(v, -1);
        }
        q.add(new int[]{y, x});
        visited[y][x] = 0;
        while (!q.isEmpty()) {
            int[] curr = q.poll();
            for (int[] dm : d) {
                int ny = curr[0] + dm[0];
                int nx = curr[1] + dm[1];
                if (0 > ny || ny >= N || 0 > nx || nx >= M || visited[ny][nx] != -1 || map[ny][nx].equals("X")) continue;
                visited[ny][nx] = visited[curr[0]][curr[1]] + 1;
                if (map[ny][nx].equals(target)) {
                    return visited[ny][nx];
                }
                q.add(new int[]{ny, nx});
            }
        }
        return -1;
    }
}
