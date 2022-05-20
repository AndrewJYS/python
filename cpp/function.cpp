#include <iostream>
using namespace std;

struct node {
    int a;
    node(int a): a(a){};
};

void changeNode(node nd) {
    nd.a = 2;
}

class class1 {
public:
    int num;
    class1() {
        num = 1;
    }
};

void changeClass(class1 c) {
    c.num = 2;
}

int main(){
    node one(1);
    cout << one.a << endl;  //output 1
    changeNode(one);
    cout << one.a << endl;  //output 1

    class1 c;
    cout << c.num << endl;  //output 1
    changeClass(c);
    cout << c.num << endl;  //output 1


    return 0;
}
