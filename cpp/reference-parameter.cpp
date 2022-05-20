#include <iostream>
using namespace std;

void f(int& num) {
    num++;
}

int main() {
    int a = 6;
    cout << a << endl;  //output 6
    f(a);
    cout << a << endl;  //output 7
    return 0;
}

