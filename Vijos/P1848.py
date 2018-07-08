n,x = map(int, raw_input().split())

count = 0
for i in range(1,n+1):
    while i != 0:
        if i % 10 == x:
            count += 1
        i = i // 10
print(count)

# #include<iostream>
# using namespace std;
#
# int main () {
#
#     int n=0,x=0;
#     int count=0;
#     cin>>n>>x;
#     for(int i=1;i<=n;i++) {
#         int k=i;
#         while(k!=0){
#             if(k%10 == x)
#                 count++;
#             k /= 10;
#         }
#     }
#     cout<<count;
# }