#include <iostream>
#include <cmath>
#include<typeinfo>
using namespace std;

int main()
{
    cout << 7 / 3 << endl;  //2
    cout << (double)7 / 3 << endl; // 2.33333
    cout << 7 / 3.0 << endl; // 2.33333

    cout << pow(2,4) << endl;
    cout << typeid(pow(2,4)).name() << endl; // d : double

    return 0;
}
