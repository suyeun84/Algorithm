import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException, NumberFormatException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        StringBuilder sb = new StringBuilder();

        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list.add(Integer.parseInt(st.nextToken()));
        }

        int start = 0;
        int end = n-1;
        int answer1 = 0;
        int answer2 = 0;
        int min_value = Integer.MAX_VALUE;

        while (start < end) {
            int temp = list.get(start) + list.get(end);
            if (Math.abs(temp) < min_value) {
                min_value = Math.abs(temp);
                answer1 = list.get(start);
                answer2 = list.get(end);
            }
            if (temp < 0) {
                start += 1;
            } else if (temp > 0) {
                end -= 1;
            } else {
                break;
            }
        }
        sb.append(answer1 + " " + answer2);
        System.out.println(sb.toString());
    }
}