import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException, NumberFormatException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int[] arr = new int[n];
        int start = 0, end = n-1;
        int[] answer = new int[2];
        int min_value = Integer.MAX_VALUE;
        
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        while (start < end) {
            int temp = arr[start] + arr[end];
            if (Math.abs(temp) < min_value) {
                min_value = Math.abs(temp);
                answer[0] = arr[start];
                answer[1] = arr[end];
            }
            if (temp < 0) {
                start += 1;
            } else if (temp > 0) {
                end -= 1;
            } else {
                break;
            }
        }
        System.out.println(answer[0] + " " + answer[1]);
    }
}