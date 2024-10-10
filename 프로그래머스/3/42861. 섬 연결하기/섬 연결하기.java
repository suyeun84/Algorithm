import java.util.*;
class Solution {
    public int solution(int n, int[][] costs) {
        int answer = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[2] - o2[2]);
        for (int[] cost: costs) {
            pq.add(cost);
        }
        int[] visited = new int[n];
        Arrays.fill(visited, -1);
        while (!pq.isEmpty()) {
            int[] cost = pq.poll();
            int a = cost[0], b = cost[1], price = cost[2];
            if (visited[a]==-1 && visited[b]==-1) {
                visited[a] = Math.min(a, b);
                visited[b] = Math.min(a, b);
                answer += price;
            } else if (visited[a]==-1 && visited[b]!=-1) {
                visited[a] = visited[b];
                answer += price;
            } else if (visited[a]!=-1 && visited[b]==-1) {
                visited[b] = visited[a];
                answer += price;
            } else {
                if (visited[a] != visited[b]) {
                    answer += price;
                    // visited[a] = Math.min(visited[a], visited[b]);
                    // visited[b] = Math.min(visited[a], visited[b]);
                    int num = Math.max(visited[a], visited[b]);
                    for (int i = 0; i < n; i++) {
                        if (visited[i] == num) {
                            visited[i] = Math.min(visited[a], visited[b]);
                        }
                    }
                }
            }
        }
        
        return answer;
    }
}