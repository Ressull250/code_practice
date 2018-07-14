#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;

bool judger(string s1, string s2, string s3);

int main () {
    int n;
    string s1,s2,s3;
    cin>>n>>s1>>s2>>s3;

    if(judger(s1,s2,s3)){
        reverse(s1.begin(), s1.end());
        cout<<s1;
    }
    else if(judger(s2,s1,s3)){
        reverse(s2.begin(), s2.end());
        cout<<s2;
    }else if(judger(s3,s2,s1)){
        reverse(s3.begin(), s3.end());
        cout<<s3;
    }else if(judger(s1,s3,s2)){
        reverse(s1.begin(), s1.end());
        cout<<s1;
    }
    else if(judger(s2,s3,s1)){
        reverse(s2.begin(), s2.end());
        cout<<s2;
    }
    else if(judger(s3,s1,s2)){
        reverse(s3.begin(), s3.end());
        cout<<s3;
    }
}

bool judger(string s1, string s2, string s3){
    reverse(s1.begin(), s1.end());
    int t1,t2;

    for (int j = 0; j <= 6; ++j) {
        for(int i=0; i<s1.length(); i++){
            t1 = (s2[i] + j - 'a' + 26)%26;
            t2 = (s3[i] - j - 'a' + 26)%26;
            if(t1!=t2 || t2!=(s1[i]-'a')){
                break;
            }
            if(i==s1.length()-1){
                return true;
            }
        }
    }
    return false;
}