#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(const char* s) {
    bool answer = true;
    int length = strlen(s);
    int a = 0;
    
    for(int i = 0; i<length; i++)
    {
        (s[i] == '(') ? a++ : a--;
        if(a < 0) return false;
    }
    
    if(a) return false;

    return answer;
}