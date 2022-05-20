#include <iostream>
using namespace std;

void f1(const int a) {
    //a++; //报错
}

void f2(const int& a) {
    //a++; //报错
}

const int& f3() { //函数前的const表明返回值不能改变
    int c = 5;
    return c;
}

int main() {
    int a = 1;
    f1(a);
    f2(a);

    f3() = 20; //报错

    return 0;
}
