#include <iostream>
using namespace std;

void f1(int num1);
void f2();
void f3();
void f4();

void pointer(int* num) {
    int* newPointer = new int(6);
    num = newPointer;
}

void f1(int num1) {
    num1++;
}

int main() {

    int* p = new int(12);
    pointer(p);
    cout << *p << endl;  // output 12

    int num1 = 4;
    cout << num1 << endl; // 4
    f1(num1);
    cout << num1 << endl; // 4

    f2();
    f3();

    f4();  // output 2
    f4();  // output 3

    return 0;
}

int y;

void f2() {
    y++;
}

void f3() {
    cout << y << endl;
}

void f4() {
    static int x = 1;
    x++;
    cout << x << endl;
}
