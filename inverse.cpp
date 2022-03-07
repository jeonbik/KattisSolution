#include <iostream>
#include<math.h>
#include <map>
#include <string>
using namespace std;

int main()
{
    map<int,int> dict;
    dict[1] = 1;
    dict[2] = 2;
    dict[6] = 3;
    dict[24] = 4;
    dict[120] = 5;
    dict [720] = 6;

    //  = {{1, 1},{2,2},{6,3},{24,4},{120,5},{720,6}};
string num;
cin >> num;
if (num.length() <= 3 && stoi(num) <= 720){
   int value = dict[stoi(num)] ;
   cout<<value;
}
else{
    //string numtostring = to_string(num);
    int length = num.length();
    int number = 7;
    double total_sum = 4 * log10(2) + 2 * log10(3) + log10(5);
    while(true){
        total_sum += log10(number);
        number ++;
        if (total_sum > length){
            cout<<(number-2);
            break;
        }

    }
}
}