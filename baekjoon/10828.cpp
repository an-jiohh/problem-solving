#include<iostream>
#include<stack>

using namespace std;

int main(void){
    stack<int> s;

    int n = 0;
    scanf("%d",&n);
    string in;
    int target = 0;
    for(int i = 0; i < n; i++){
        cin >> in;
        if  (in == "push") {
            int n = 0;
            scanf("%d", &n);
            s.push(n);
        }
        else if (in == "pop") {
            if (s.empty()){
                printf("%d\n", -1);
            }
            else {
                printf("%d\n", s.top());
                s.pop();
            }
        }
        else if (in == "size") printf("%lu\n", s.size());
        else if (in == "empty") printf("%d\n", s.empty());
        else if (in == "top"){
            if (s.empty()){
                printf("%d\n", -1);
            }
            else {
                printf("%d\n", s.top());
            }
        } 
    }
}