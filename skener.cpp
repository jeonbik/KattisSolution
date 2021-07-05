#include <iostream>
using namespace std;

int main()
{
    int r,c ,zr,zc;
    cin>>r>>c>>zr>>zc;
    char array_input[r][c];
    for (int i = 0;i <r;i++){
        for (int j = 0; j < c; j++){
            cin>>array_input[i][j];
        }
    }

    for (int i  = 0; i< r*zr;i++){
        for (int j = 0; j< c*zc;j++){
            cout<<array_input[i/zr][j/zc];
        }
        cout<<"\n";
    }
    return 0;
}