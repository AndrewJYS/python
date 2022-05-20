#include <iostream>
using namespace std;

class GeometricObject {
public:
    void info() {
        cout << "GeometricObject" << endl;
    }
};

class Triangle: public GeometricObject {
public:
    void info() {
        cout << "Triangle" << endl;
    }
};

int main() {
    GeometricObject* g = new GeometricObject();
    g->info();  // GeometricObject
    GeometricObject* g2 = new Triangle();
    g2->info(); // GeometricObject

    return 0;
}
