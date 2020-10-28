#include <stdio.h>
#include <sys/time.h>
int main(){
    struct timeval tv1, tv2;
    gettimeofday(&tv1, NULL);
    int a = 0;
    for(int i=0; i<10000; i++)
        a += i;
    gettimeofday(&tv2, NULL);
    double delta = (double)(tv2.tv_usec - tv1.tv_usec) / 1000000 +
         (double) (tv2.tv_sec - tv1.tv_sec);
    printf("%f", delta);
}