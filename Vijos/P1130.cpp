#include <iostream>
#include <queue>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;
void next(int n, int &count);

int main () {

    int n,count=1;
    cin>>n;

    next(n,count);

    cout<<count;
}

void next(int n, int &count){
    for(int i=1; i<=n/2; i++){
        count++;
        next(i, count);
    }
}

