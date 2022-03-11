#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
    char s[1000000+5];
    bool got;
    int i,j,len;
    while(gets(s)&&s[0]!='.'){
        len = strlen(s);
        got = true;
        for(i=1;i<len-1;i++){
            if(len%i!=0)continue;
            for(j=i;j<len;j++)
                if(s[j]!=s[j%i]){
                    got = false;
                    break;
                }
            if(got)break;
            got = true;
        }
    if(got)printf("%d\n",len/i);
    else printf("%d\n",len);
    }
    return 0;
}


#naive 
while True:
    val = input()
    if val == ".":
        break
    input_len = len(val)
    track = True
    for i in range(1,input_len-1):
        if input_len%i != 0:
            continue
        for j in range(i,input_len):
            if val[j] != val[j%i]:
                track = False
                break
            if track: break
        track = True
    if track: print(input_len/i)
    else: print(input_len)
