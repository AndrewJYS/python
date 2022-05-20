#include <unordered_set>
#include <iostream>
using namespace std;

int main()
{
    unordered_set<int> a = {1,2,3,3};
    for (auto& item: a)
        cout << item << " "; //3 2 1
    cout << endl;

    a.emplace(5);
    for (auto p = a.begin(); p != a.end(); p++)
        cout << *p << " ";  //5 3 2 1
    cout << endl;

    a.erase(3);
    for (auto p = a.begin(); p != a.end(); p++)
        cout << *p << " ";  //5 2 1
    cout << endl;

    return 0;
}
