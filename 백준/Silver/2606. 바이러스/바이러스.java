import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int result;
    static int comNum;
    static boolean[] visit;
    static int[][] branch;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        comNum = Integer.parseInt(br.readLine());
        int network = Integer.parseInt(br.readLine());
        visit = new boolean[comNum+1];
        branch = new int[comNum+1][comNum+1];
        for (int i = 0; i < network; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            branch[a][b] = branch[b][a] = 1;
        }
        result = 0;
        dfs(1);
        System.out.println(result);
    }

    public static void dfs(int start){
        visit[start] = true;
        for (int i = 1; i < comNum + 1; i++) {
            if((branch[start][i] == 1) && (visit[i] == false)){
                result++;
                dfs(i);
            }
        }
    }
}