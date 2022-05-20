#include <iostream>
#include<typeinfo>
using namespace std;

int main()
{
    int a = 8;
    cout << typeid(a).name() << endl;
    cout << &a << endl;
    return 0;
}
