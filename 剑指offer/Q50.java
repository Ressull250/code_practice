public class Q50 {
    public int FirstNotRepeatingChar(String str) {

        int[] table = new int[128];
        for (int i=0; i<str.length(); i++){
            table[str.charAt(i)]++;
        }
        for (int i=0; i<str.length(); i++){
            if (table[str.charAt(i)] == 1)
                return i;
        }
        return -1;
    }
}