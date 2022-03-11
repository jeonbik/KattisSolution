import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
// import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Binary 
{
    public static void main (String[] args)
    {

        try (Scanner scan = new Scanner(System.in)) {
            while (true)
            {
                int jack = scan.nextInt();
                int jill = scan.nextInt();
                if (jack <= 0 || jill <= 0) break;
                Set <String> jack_set = new HashSet<String>();
                Set <String> jill_set = new HashSet<String>();

              //fill Jack's CDs
              for(int i = 0; i < jack;i++){
                  jack_set.add(scan.nextLine());
              }

              for(int i = 0; i <= jill;i++){
                  jill_set.add(scan.nextLine());
              }

              Set<String> intersection = new HashSet<String>(jack_set); 
              intersection.retainAll(jill_set);

              ArrayList<Integer> ans = new ArrayList<Integer>();
              ans.add(intersection.size());

              for(int i = 0; i < ans.size();i++)System.out.println(ans.get(i));
            

            }
            // scan.close();
        }
    }

    public static boolean binarySearch(List<Integer> arrayList, int length, int val)
    {
        int low = 0;
        int high = length;
        while (low < high)
        {
            int mid = high - low/2;
            int midVal = arrayList.get(mid);
            if ( midVal == val)
                return true;

            else if (midVal < val)
                low = mid + 1;
            
            else
                high = mid - 1;
        }
        return false;
    }
}