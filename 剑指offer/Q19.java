public class Q19 {

    public boolean match(char[] str, char[] pattern) {

        return matchHelper(str, pattern, 0, 0);
    }

    public boolean matchHelper(char[] str, char[] pattern, int strofs, int patofs){

        if (strofs<str.length && patofs<pattern.length){
            if (str[strofs] == pattern[patofs] || pattern[patofs] == '.'){
                if (patofs+1 < pattern.length && pattern[patofs+1] == '*'){
                    return matchHelper(str, pattern, strofs+1, patofs+2) ||
                            matchHelper(str, pattern, strofs, patofs+2) ||
                            matchHelper(str, pattern, strofs+1, patofs);
                }
                else
                    return matchHelper(str, pattern, strofs+1, patofs+1);
            }
            else if (patofs+1 < pattern.length && pattern[patofs+1] == '*')
                return matchHelper(str, pattern, strofs, patofs+2);
            else
                return false;
        }

        if (strofs == str.length && patofs == pattern.length)
            return true;
        //str位数多
        if (strofs < str.length) return false;
        //pat位数多
        while (patofs+1 < pattern.length){
            if (pattern[patofs+1] == '*'){
                patofs += 2;
                if (patofs == pattern.length)
                    return true;
            }
            else
                return false;
        }
        return false;
    }
}
