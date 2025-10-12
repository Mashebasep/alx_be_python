from polymorphism_demo import Shape,Rectangle, Circle
def main():
    rectangle = Rectangle(10, 5)
    circle = Circle(7)
    print(f"The area of the Rectangle is: {rectangle.are()}")
    print(f"The area of the Circle is: {circle.area()}")

