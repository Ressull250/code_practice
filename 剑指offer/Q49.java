public class Q49 {
    public int GetUglyNumber_Solution(int index) {
        if (index <= 0) return 0;
        int[] table = new int[index];
        table[0] = 1;
        int i2=0, i3=0, i5=0;
        for (int i=1; i<index; i++){
            table[i] = Math.min(table[i5]*5, Math.min(table[i2]*2, table[i3]*3));
            //排除掉2*3 和 3*2
            if (table[i] == table[i2]*2) i2++;
            if (table[i] == table[i3]*3) i3++;
            if (table[i] == table[i5]*5) i5++;
        }
        return table[index-1];
    }
}