import java.util.Arrays;

public class Q45 {

    public String PrintMinNumber(int [] numbers) {
        if (numbers == null) return "";
        return Arrays.stream(numbers).mapToObj(String::valueOf).sorted(
                //我的比较函数比较僵，直接 s1+s2.campareTo(s2+s1) 简洁
                Q45::mycampare
        ).reduce((s1, s2) -> s1 + s2).orElse("");
    }

    public static int mycampare(String s1, String s2){
        for (int i=0; i<Math.min(s1.length(), s2.length()); i++){
            if (s1.charAt(i) < s2.charAt(i))
                return -1;
            else if (s1.charAt(i) > s2.charAt(i))
                return 1;
        }
        if (s1.length() < s2.length()){
            return campareNext(s1, s2);
        }
        else
            return -campareNext(s2, s1);
    }

    public static int campareNext(String s1, String s2){
        assert s1.length()<=s2.length();
        char last = s1.charAt(s1.length()-1);
        for (int i=s1.length(); i<s2.length(); i++){
            if (last < s2.charAt(i))
                return -1;
            else if (last > s2.charAt(i))
                return 1;
        }
        return 1;
    }
}