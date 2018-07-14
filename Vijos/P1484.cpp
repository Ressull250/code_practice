#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;

int main () {
    string s;
    cin>>s;
    int sum=0,k=1;

    for(int i=0;i<s.length()-1;i++){
        if(s[i]=='-') continue;
        sum += (s[i] - '0')*k;
        k++;
    }

    int t = sum%11;
    if(t == (s[s.length()-1] - '0') || (t==10 && s[s.length()-1]=='X'))
        cout<<"Right";
    else{
        s = s.substr(0, s.length()-1);
        if(t==10)
            s.append("X");
        else
            s.append(1, '0'+t);

        cout<<s;
    }
}