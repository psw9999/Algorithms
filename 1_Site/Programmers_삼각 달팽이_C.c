#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int n) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)calloc(n * (n+1) / 2, sizeof(int));
    int temp[n][n];
    int re = n;
    int col = 0, row = -1;
    int a = 0, b = 0, c = 0, num = 0;
    for(a = 0;a < re;a++){
        b = re - a;
        if(c % 3 == 0){
            while (b-- > 0)
                temp[++row][col] = ++num;
        }
        else if(c % 3 == 1){
            while (b-- > 0)
                 temp[row][++col] = ++num;
        }
        else{
            while (b-- > 0)
                temp[--row][--col] = ++num;
        }
        c++;
    }
    int count = 0;
    for(int i = 0;i < n;i++){
        for(int j = 0;j <= i;j++)
            answer[count++] = temp[i][j];
    }
    return answer;
}