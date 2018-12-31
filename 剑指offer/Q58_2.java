public class Q58_2 {
    public String LeftRotateString(String str,int n) {
        if (str == null || str.length()==0) return str;
        n = n%str.length();
        return str.substring(n, str.length()) + str.substring(0, n);
    }
}