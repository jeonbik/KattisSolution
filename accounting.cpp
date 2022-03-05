#include <iostream>
using namespace std;

int main()
{
    int q,n ;
    cin>>q>>n;
    int my_array[n] = {0};
    for (int i  = 0; i< n;i++){
        string command;
        getline(cin,command);
        string val[0];
        if (val == "SET"){
            int idx,change;
            idx = int(command[1]);
            change = int(command[2]);
            my_array[idx] = change;

        }
        else if (val == "RESTART"){
            my_array[n] = {int(command[1])};
        }
        else{
            cout<<my_array[int(command[1])];
        }

    return 0;
// }

// holdings = [0] * (n+1)
// for i in range(q):
//     command = input().split()
//     if command [ 0] == "SET":
//         a,b = map(int,command[1:])
//         holdings[a] = b
//     elif command [0] == "RESTART":
//         a = int(command[1])
//         holdings = [a] * (n+1)
//     else:
//         print(holdings[int(command[1])])