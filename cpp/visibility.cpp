#include <iostream>
using namespace std;

class class1 {
public:
    class1() {
        num1 = 0;
        num2 = 0;
        num3 = 0;
    }

    int num1;

protected:
    int num2;

private:
    int num3;
};

int main() {
    class1 c;
    cout << c.num1 << endl;
    cout << c.num2 << endl;  // 报错
    cout << c.num3 << endl;  // 报错

    return 0;
}
