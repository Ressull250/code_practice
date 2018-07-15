#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;

int main () {
    int a[10];
    int count=0;
    for(int i=100; i<333; i++){
        int n1=i,n2=i*2,n3=i*3;
        a[n1/100]=1;
        a[n1/10%10]=1;
        a[n1%10]=1;
        a[n2/100]=1;
        a[n2/10%10]=1;
        a[n2%10]=1;
        a[n3/100]=1;
        a[n3/10%10]=1;
        a[n3%10]=1;
        for(int j=1; j<10; j++){
            count+=a[j];
            a[j]=0;
        }
        if(count==9){
            cout<<n1<<" "<<n2<<" "<<n3<<endl;
        }
        count=0;
    }
}
