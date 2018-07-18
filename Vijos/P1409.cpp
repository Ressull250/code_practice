#include <iostream>
#include <queue>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;

int main () {
    int max,n,t;
    cin>>max>>n;

    vector<int> list;
    for(int i=0; i<n; i++) {
        cin >> t;
        list.push_back(t);
    }

    sort(list.begin(), list.end());

    int l=0, r=n-1, count=0;
    while (l <= r){
        if(list[l]+list[r]<=max){
            l++;
            r--;
        }
        else{
            r--;
        }
        count++;
    }

    cout<<count;
}

