#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
using namespace std;

int main() {
    int jack, jill,number;

    while(cin >>jack  >> jill && jack != 0 && jill != 0) {
        vector<int> jack_collection, jill_collection, answer;
        for(int i = 0; i < jack; i++) {
            cin >> number;
            jack_collection.push_back(number);
        }
        for(int i = 0; i < jill; i++) {
            cin >> number;
            jill_collection.push_back(number);
        }
        set_intersection(jack_collection.begin(), jack_collection.end(), 
        jill_collection.begin(), jill_collection.end(), back_inserter(answer));
        cout << answer.size() << endl;
    }
    return 0;
}
