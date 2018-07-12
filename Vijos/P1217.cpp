#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main () {

    char t;
    vector<char> list;
    int left=0,right=0;

    while(true){
        cin>>t;
        if(t=='E') break;
        if(t=='W' || t=='L')
            list.push_back(t);
    }

    for (int i = 0; i < list.size(); ++i) {
        t = list[i];
        if(t=='W') left++;
        else right++;

        if((left>=11 || right>=11) && abs(left-right) >= 2){
            cout<<left<<":"<<right<<endl;
            left=right=0;
        }
    }
    cout<<left<<":"<<right<<endl<<endl;

    left=right=0;
    for (int i = 0; i < list.size(); ++i) {
        t = list[i];
        if(t=='W') left++;
        else right++;

        if((left>=21 || right>=21) && abs(left-right) >= 2){
            cout<<left<<":"<<right<<endl;
            left=right=0;
        }
    }
    cout<<left<<":"<<right<<endl<<endl;
}