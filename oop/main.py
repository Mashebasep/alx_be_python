from polymorphism_demo import Shape,Rectangle, Circle
def main():
    shapes = [Rectangle(10, 5, Circle(7))]
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")
    rectangle = Rectangle(10, 5)
    circle = Circle(7)
    print(f"The area of the Rectangle is: {rectangle.are()}")
    print(f"The area of the Circle is: {circle.area()}")

