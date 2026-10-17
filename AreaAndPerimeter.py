# 24th github project --> Area and Perimeter Finder
print("----------Area and Perimeter Finder----------")
import math


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter a valid number.")


def circle():
    r = get_number("Radius: ")
    print(f"Area: {math.pi * r ** 2:.2f}")
    print(f"Perimeter: {2 * math.pi * r:.2f}")


def rectangle():
    l = get_number("Length: ")
    w = get_number("Width: ")
    print(f"Area: {l * w:.2f}")
    print(f"Perimeter: {2 * (l + w):.2f}")


def triangle():
    b = get_number("Base: ")
    h = get_number("Height: ")
    a = get_number("Side A: ")
    c = get_number("Side C: ")
    print(f"Area: {0.5 * b * h:.2f}")
    print(f"Perimeter: {a + b + c:.2f}")


def square():
    s = get_number("Side: ")
    print(f"Area: {s ** 2:.2f}")
    print(f"Perimeter: {4 * s:.2f}")


def main():
    shapes = {
        "1": ("Circle", circle),
        "2": ("Rectangle", rectangle),
        "3": ("Triangle", triangle),
        "4": ("Square", square),
    }

    while True:
        print("\n1. Circle  2. Rectangle  3. Triangle  4. Square  5. Quit")
        choice = input("Choose: ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice in shapes:
            name, func = shapes[choice]
            print(f"\n{name}")
            func()
        else:
            print("Invalid choice.")



main()