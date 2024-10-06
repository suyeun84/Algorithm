import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException, NumberFormatException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine(), " "); //배열
        Stack<int[]> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < n; i++) {
            int top = Integer.parseInt(st.nextToken());
            if(!stack.isEmpty()) {
                if (stack.peek()[0] >= top) {
                    sb.append(stack.peek()[1]+" ");
                } else {
                    while (!stack.isEmpty()) {
                        if (stack.peek()[0] >= top) {
                            sb.append(stack.peek()[1]+" ");
                            break;
                        }
                        stack.pop();
                    }
                }
            }
            if (stack.isEmpty()) {
                sb.append("0 ");
            }
            stack.push(new int[] {top, i+1});
        }
        System.out.println(sb.toString());
    }
}