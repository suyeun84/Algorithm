import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        String L = st.nextToken();
        int cnt = 0;
        int num = 1;
        while (cnt < N) {
            if (String.valueOf(num).contains(L)) {
                num += 1;
                continue;
            }
            num += 1;
            cnt += 1;
        }
        System.out.print(num-1+"");
        br.close();
    }
}
