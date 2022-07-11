#include<iostream>
#include <algorithm> 

using namespace std;

int binarySearch(int arr[], int len, int key){
    int start = 0;
    int end = len - 1;
    int mid;

    while(end - start >= 0){
        mid = (start+end) / 2;
        if(arr[mid] == key){
            return 1;
        }
        else if(arr[mid] > key) {
            end = mid - 1;
        }
        else {
            start = mid + 1;
        }
    }
    return 0;
}

int main(void){
    int num = 0;
    scanf("%d",&num);
    int arr[num];
    for(int i = 0; i < num; i++){
        scanf("%d", &arr[i]);
    }
    sort(arr, arr + num);

    int searchNum = 0;
    scanf("%d", &searchNum);
    for(int i = 0; i < searchNum; i++){
        int find = 0;
        scanf("%d",&find);
        printf("%d\n",binarySearch(arr,num,find));
    }

    return 0;
}