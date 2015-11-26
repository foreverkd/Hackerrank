#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int N;
    unsigned int arr[N];
    unsigned long long int sum = 0;
    scanf("%d",&N);
    for(int i=0;i<N;i++)
        scanf("%d",&arr[i]);
    for(int i=0;i<N;i++)
        sum+=arr[i];
    printf("%llu",sum);
    return 0;
}
