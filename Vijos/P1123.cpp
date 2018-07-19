#include <iostream>
#include <queue>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;

int main () {

    int a[1000];
    int n,t=0,count=0;
    cin>>n;

    for(int i=0; i<n; i++){
        cin>>a[i];
        t+=a[i];
    }
    t = t/n;
    for(int i=0; i<n; i++){
        if(a[i]!=t){
            count++;
            a[i+1] += (a[i] - t);
        }
    }
    cout<<count;

}

