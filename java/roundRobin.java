import java.util.*;

class TestClass {
    public static void main(String args[] ) throws Exception {

        Scanner s = new Scanner(System.in);
        String input = s.nextLine();
        int n = Integer.parseInt(input.split(" ")[0]);
        int c = Integer.parseInt(input.split(" ")[1]);
        int[] process = new int[n], waitTime = new int[n], endRank = new int[n];
        
        String[] inputArr = s.nextLine().split(" ");
        for (int i = 0; i < n; i++)
            process[i] = Integer.parseInt(inputArr[i]);
            
        int done = 0, cdone = 0, current = 0, time = 0;
        Arrays.fill(waitTime, -1);
        
        while (done < n) {
            cdone = 0;
            while (cdone < c) {
                if (waitTime[current] == -1)
                    waitTime[current] = time;
                    
                if (process[current] > c) {
                    process[current] -= c;
                    cdone += c;
                    time += c;
                }
                
                else if (process[current] != 0) {
                    cdone += process[current];
                    time += process[current];
                    process[current] = 0;
                    endRank[current] = ++done;
                }
                
                current =  (current + 1) % n;   
            }
        }
        
        int i = 0, q = Integer.parseInt(s.nextLine());
        while (i < q) {
            i++;
            input = s.nextLine();
            int m = Integer.parseInt(input.split(" ")[0]);
            int d = Integer.parseInt(input.split(" ")[1]);
            if (m == 1)
                System.out.println(waitTime[d - 1]);
            else
                System.out.println(endRank[d - 1]);
        }
    }
}
