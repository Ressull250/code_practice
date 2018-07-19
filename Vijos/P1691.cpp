#include <iostream>
#include <queue>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;

int main () {

    /**
     * 当上下两侧点数相等时，输油管在中间移动距离之和不变
     * 移动至偏向任意一侧，距离之和增加，故中位数时为输油管的位置
     */

    vector<int> a;
    int n,x,y;
    long long ans=0;
    cin>>n;

    for(int i=0; i<n; i++){
        cin>>x>>y;
        a.push_back(y);
    }

    sort(a.begin(), a.end());

    y = n/2;

    for(int i=0; i<n; i++){
        ans += abs(a[i]-a[y]);
    }

    cout<<ans;
}

