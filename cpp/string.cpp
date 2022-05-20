#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s = "123";
    s.append("124").append("125");
    cout << s << endl;

    s = "0123456789";
    cout << s.substr(4) << endl; //456789
    cout << s.substr(4,3) << endl;  //456

    s = "0123456789";
    cout << s.find("12") << endl; // output 1
    cout << (s.find("90", 8) == string::npos) << endl; // output 1

    return 0;
}
