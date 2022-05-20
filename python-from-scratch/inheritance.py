class GeometricObject:
    def info(self):
        print("GeometricObject")

    def superFunc(self):
        print("Geometric")

class Triangle(GeometricObject):
    def info(self):
        print("Triangle")

triangle = Triangle()
triangle.info() # Triangle
triangle.superFunc() # Geometric

