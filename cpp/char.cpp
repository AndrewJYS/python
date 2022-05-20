#include <iostream>
using namespace std;

int main()
{
    cout << '$' << endl;
    cout.put('$');
    cout << endl;

    char ch = '&';
    int i = ch;
    cout << i << endl;

    char ch1 = '\012';
    char ch2 = '\xa';
    cout << ch1 << " " << ch2;

    cout << "enter" << endl;

    return 0;
}
