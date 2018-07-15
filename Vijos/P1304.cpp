#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;
bool judge(string s);
int toNum(char num, int n);
char tochar(int num);

int main () {
    int n,count=0; string s;
    string s2,ns;
    cin>>n>>s;
    s2=s;

    while(!judge(s)){
        reverse(s.begin(), s.end());
        int c=0,r=0;

        for(int i=s.length()-1; i>=0; --i){
            r = (toNum(s[i],n) + toNum(s2[i], n) + c)%n;
            c = (toNum(s[i],n) + toNum(s2[i], n) + c)/n;;
            ns.insert(0, 1, tochar(r));
        }
        if(c!=0){
            ns.insert(0, 1, tochar(c));
        }
        s2=ns; s=ns; ns="";
        count++;
        if(count>=30){
            cout<<"Impossible!";
            return 0;
        }
    }

    cout<<"STEP="<<count;
}

char tochar(int num){
    if(num>=10){
        return num-10+'A';
    }
    else{
        return '0'+num;
    }
}

int toNum(char num, int n){
    if(n == 16){
        if(num>='0' && num<='9'){
            return num - '0';
        }
        else{
            return num - 'A' + 10;
        }
    }
    else{
        return num - '0';
    }
}

bool judge(string s){
    string s2 = s;
    reverse(s.begin(), s.end());
    return s==s2;
}