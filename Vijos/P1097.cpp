#include <iostream>
#include <queue>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;

int main () {
    int n,t;
    cin>>n;

    priority_queue<int,vector<int>,greater<int> > list;

    for(int i=0; i<n; i++){
        cin>>t;
        list.push(t);
    }

    int sum=0;
    while(list.size()>=2){
        t = list.top();
        list.pop();
        t += list.top();
        list.pop();
        sum += t;
        list.push(t);
    }

    cout<<sum;
}

