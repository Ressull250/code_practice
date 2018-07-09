#include<iostream>
using namespace std;

int main () {

    int n=0;
    string name;
    int g1,g2,article;
    string leader,western;
    cin>>n;

    int maxmoney = 0, total = 0;
    string maxname = "";

    for(int i=0;i<n;i++){
        int money = 0;
        cin>>name>>g1>>g2>>leader>>western>>article;

        if(g1>80){
            if(article>0){
                money+=8000;
            }
            if(g1>85){
                if(g2>80){
                    money+=4000;
                }
                if(western=="Y"){
                    money+=1000;
                }
                if(g1>90){
                    money+=2000;
                }
            }
        }

        if(leader=="Y" && g2>80){
            money+=850;
        }

        if(money>maxmoney){
            maxmoney = money;
            maxname = name;
        }

        total+=money;
    }

    cout<<maxname<<endl<<maxmoney<<endl<<total<<endl;
}