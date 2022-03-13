#include <iostream>
#include <map>
#include <string>
#include <iterator>
#include <algorithm>
using namespace std;

int main(){
    int n,a,b,i,j;
    map<int,string> my_map;
    cin >> n;
    for (i = 1; i <n+1;i++){
        string words;
        cin>>words;
        my_map.insert(pair<int,string>(i,words));

    }
    for (j = 0; j < n-1;j++){
        cin>>a>>b;
        my_map[a] = my_map[a] + my_map[b];
        
        my_map.erase(b);
    }
    map<int, string>::iterator it = my_map.begin();
 while (it != my_map.end())
    {

        // Accessing VALUE from element pointed by it.
        string val = it->second;
        cout << val <<endl;
        // Increment the Iterator to point to next entry
        it++;
    }
return 0;

}


