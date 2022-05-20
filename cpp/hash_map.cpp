#include <unordered_map>
#include <iostream>
using namespace std;

int main()
{
    unordered_map<string, int> a;
    a["num1"] = 1;
    a.emplace("num2", 2);

    cout << a["num1"] << endl; //output 1
    cout << a["num3"] << endl; //output 0

    cout << (a.find("num1") != a.end()? "found" : "not found") << endl; //found
    cout << (a.find("num3") != a.end()? "found" : "not found") << endl; //found
    cout << (a.find("3") != a.end()? "found" : "not found") << endl; //not found
    cout << (a.find("3") != a.end()? "found" : "not found") << endl; //not found


    a.erase("num2");
    cout << (a.find("num2") != a.end()? "found" : "not found") << endl; //not found

    a.clear();
    cout << (a.empty()? "True" : "False") << endl; // True


    return 0;
}
