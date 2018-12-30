public class Q48 {

    public int maxNonReapeatSubstr(String s){
        if (s == null || s.length() == 0) return 0;
        int[] table = new int[26];
        int maxx = Integer.MIN_VALUE;
        int cur = 0, begin = 0;

        for (int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if (table[c-'a'] == 0){
                table[c-'a'] ++;
                cur++;
                maxx = Math.max(cur, maxx);
            }
            else{
                while (s.charAt(begin) != c){
                    table[s.charAt(begin)-'a'] = 0;
                    begin++;
                    cur--;
                }
                table[s.charAt(begin)-'a'] = 0;
                begin++;
                cur--;
            }
        }
        return maxx;
    }
}
