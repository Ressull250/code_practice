#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main () {

    int n=0,t=0,count=0;
    int area[20001];
    cin>>n;

    vector<int> list;

    for(int i=0; i<n; i++){
        cin>>t;
        list.push_back(t);
    }

    sort(list.begin(),list.end());

    for(int i=0; i<n-2; i++){
        for(int j=i+1; j<n-1; j++){
            for (int k=j+1; k<n; ++k) {
                if(list[i]+list[j] == list[k]){
                    if(area[list[k]] == 0){
                        count++;
                        area[list[k]] = 1;
                    }
                }
                if(list[i]+list[j] < list[k]){
                    break;
                }
            }
        }
    }

    printf("%d", count);
}