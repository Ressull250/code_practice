#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;

int main () {
    int n;
    cin>>n;
    int sum = 45;
    int total = 362880; //9!
    int t=1,tt=0; bool flag=true;

    for(int i=0; i<n; i++) {
        int a[9][9];
        flag=true;
        for (int j = 0; j < 9; j++) {
            for (int k = 0; k < 9; k++) {
                cin >> a[j][k];
            }
        }

        for (int j = 0; j < 9; j++) {
            t = 1; tt = 0;
            for (int k = 0; k < 9; k++) {
                t *= a[j][k];
                tt += a[j][k];
            }
            if (t != total || tt != sum) {
                flag = false;
            }
        }

        for (int j = 0; j < 9; j++) {
            t = 1; tt = 0;
            for (int k = 0; k < 9; k++) {
                t *= a[k][j];
                tt += a[k][j];
            }
            if (t != total || tt != sum) {
                flag = false;
            }
        }

        for (int m = 0; m < 3; m++){
            for (int n = 0; n < 3; n++) {
                t = 1; tt = 0;
                for (int k = 0; k < 9; k++) {
                    t *= a[m * 3 + k / 3][n * 3 + k % 3];
                    tt += a[m * 3 + k / 3][n * 3 + k % 3];
                }
                if (t != total || tt != sum) {
                    flag = false;
                }
            }
        }
        if(flag) cout<<"Right"<<endl;
        else cout<<"Wrong"<<endl;
    }
}

