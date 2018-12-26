public class Q20 {
    //正则表达式[+|-]A.A[e|E[+|-]A]
    //按答案的意思是A.A部分可以是.A或A.或A
    public boolean isNumeric(char[] str) {

        if (str.length == 0) return false;

        //[+|-]
        int offset = 0;
        if (str[0] == '+' || str[0] == '-')
            offset++;

        if (offset>=str.length) return false;
        //.A
        if (str[offset] == '.'){
            offset++;
            int t = scanA(str, offset);
            if (offset == t) return false;
            else offset = t;
        }//A A. A.A
        else{
            int t = scanA(str, offset);
            if (offset == t) return false;
            offset = t;
            //A之后没有true
            if (offset >= str.length)
                return true;
            else{
                //A. A.A
                if (str[offset] == '.'){
                    offset++;
                }
                offset = scanA(str, offset);
            }
        }

        //[e|E[+|-]A]
        if (offset == str.length) return true;
        else if (offset < str.length && (str[offset] == 'e' || str[offset] == 'E')){
            offset++;
            if (offset >= str.length) return false;
            if (str[offset] == '+' || str[offset] =='-'){
                offset++;
                if (offset >= str.length) return false;
            }
            int t = scanA(str, offset);
            if (offset == t) return false;
            else if (t == str.length)return true;
        }

        return false;
    }

    public int scanA(char[] str, int offset){
        while (offset < str.length && Character.isDigit(str[offset]))
            offset++;
        return offset;
    }
}
