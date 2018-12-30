public class Q43 {
    /*
    abcde
    在c出现1的次数
    c=0 ab*100
    c=1 ab*100+de+1
    c>1 ab*100+100
    */
    public int NumberOf1Between1AndN_Solution(int n) {
        int i=1, p=n;
        int before=0, cur=0, after=0;
        int count=0;

        while (p != 0){
            after = n % i;
            cur = n / i % 10;
            before = n / i / 10;

            if (cur == 0)
                count += before * i;
            else if (cur == 1)
                count += before * i + after + 1;
            else
                count += (before+1) * i;

            p /= 10;
            i *= 10;
        }

        return count;
    }
}