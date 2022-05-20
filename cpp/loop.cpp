#include <iostream>
using namespace std;

int main()
{
    string s = "admin";
    for (auto& ch : s) {
        cout << ch << " ";
    }

    return 0;
}
