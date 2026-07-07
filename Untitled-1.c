# include <stdio.h>
int linear search (int arr[],int n,int key) {
    for (int i=0; i=0; i<n; i++) {if(arr[i] ==key) {

    
    return i;}
}
int main() {
    int arr=[10,50,30,70,80,20,90,40,];
    int n=sizeof (arr)/sizeof(arr[0]);
    int key;
    printf ("enter element to search ;");
    scanf("%d,&key");
    int result = linear search (arr,n,key);
    result 0;
}