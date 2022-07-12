#include<iostream>

using namespace std;

int main(void){
    long long a, b;
    scanf("%lld %lld",&a,&b);
    if (a < b) {
        long long temp = a;
        a = b;
        b = temp;
    }
    
    while(b){
        long long n = a % b;
        a = b;
        b = n;
    }
    for(long long i = 0; i < a; i++) printf("%d",1);
    printf("\n");

    return 0;
}