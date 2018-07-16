#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
using namespace std;
void tofen(string s);
void tolian(string s);
int gcd(int x, int y);

int main () {
    string s;
    while(getline(cin,s)){
        if(s[0] == '[')
            tofen(s);
        else
            tolian(s);
    }
}

void tofen(string s){
    vector<int> list;
    for(int i=0; i<s.length(); i++){
        if(isdigit(s[i])){
            list.push_back(s[i]);
        }
    }
    int fz=1,fm=0,t=0;
    for(int i=list.size()-1; i>=0;i--){
        t=fz;
        fz=fm;
        fm=t;
        fz+=(list[i]-'0')*fm;
    }
    int gg=gcd(fz,fm);
    fz/=gg;fm/=gg;//约分为最简
    if(fm==1) printf("%d\n",fz);
    else printf("%d/%d\n",fz,fm);
}

void tolian(string s){
    stringstream ss(s);
    int fz,fm; char c;
    string s1, s2;
    auto it = s.find('/');
    if (it > s.size()) {
        s1 = s; s2 = "0";
    } else {
        s1 = s.substr(0, it);
        s2 = s.substr(it + 1, s.length() - it);
    }
    fz = atoi(s1.c_str());
    fm = atoi(s2.c_str());
    vector<int> list;
    if(fm==0) fm=1;
    while(true){
        int t=fz/fm;
        list.push_back(t);
        fz=fz-t*fm;
        if(fz==0) break;
        int tt=fz;
        fz=fm;
        fm=tt;
    }
    if(list.size()==1) printf("[%d]", list[0]);
    else{
        printf("[%d;", list[0]);
        for(int i=1; i<list.size()-1; i++){
            printf("%d,",list[i]);
        }
        printf("%d]",list[list.size()-1]);
    }
}

int gcd(int x, int y){
    int t=0;
    if(x<y){
        t=x;
        x=y;
        y=t;
    }
    int r=x%y;
    while(r){
        x=y;
        y=r;
        r=x%y;
    }
    return y;
}