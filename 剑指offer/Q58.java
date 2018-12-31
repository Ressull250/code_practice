public class Q58 {

    public String ReverseSentence(String str) {
        if (str == null) return null;
        if (str.trim().equals("")) return " ";
        String[] strs = str.split(" ");
        StringBuilder b = new StringBuilder();
        for (int i=strs.length-1; i>=0; i--){
            b.append(strs[i]);
            if (i!=0){
                b.append(" ");
            }
        }
        return b.toString();
    }
}
