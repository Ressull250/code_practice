public class Q46 {

    public int translate(int num){
        String s = Integer.toString(num);
        int[] table = new int[s.length()+1];

        table[s.length()-1] = 1;
        table[s.length()] = 1;
        for (int i=s.length()-2; i>=0; i--){
            if (i+1<s.length())
                table[i] += table[i+1];
            if (i+2<s.length() && s.charAt(i)>'0' && s.charAt(i)<='2' && s.charAt(i+1)<='5')
                table[i] += table[i+2];
        }
        return table[0];
    }
}
