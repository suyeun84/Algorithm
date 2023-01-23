import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    static int n;
    static int m;
    static int v;
    static boolean[] visit = new boolean[1001];
    static int[][] branch = new int[1001][1001];

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        n = scanner.nextInt(); //정점 개수
        m = scanner.nextInt(); //간선 개수
        v = scanner.nextInt(); //탐색 시작 정점 번호

        for (int i = 0; i < m; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            branch[a][b] = 1;
            branch[b][a] = 1;
        }
        dfs(v);
        System.out.println();
        Arrays.fill(visit,false);
        bfs();
    }
    public static void dfs(int v){
        //stack 또는 재귀
        visit[v] = true;
        System.out.print(v + " ");
        for (int i = 1; i <= n; i++) {
            if((branch[v][i] == 1) && (visit[i] == false))
                dfs(i);
        }
    }
    public static void bfs(){
        //queue
        Queue<Integer> queue = new LinkedList<>();
        queue.add(v);
        visit[v] = true;
        System.out.print(v + " ");

        while(!queue.isEmpty()){
            int poll = queue.poll();
            for (int i = 1; i <= n; i++) {
                if((branch[poll][i] == 1) && (visit[i] == false)){
                    queue.add(i);
                    visit[i] = true;
                    System.out.print(i + " ");
                }
            }
        }
    }
}