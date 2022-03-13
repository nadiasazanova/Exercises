r1 = 10
def f():
    return 3.14 *r1 ** 2
print("Circle area a = ", 3.14 * r1 **2)

r2 = 6
def f():
    return 3.14 *r2 ** 2
print("Circle area b = ", 3.14 * r2 **2)

r3 = 4
def f():
    return 3.14 *r3 ** 2
print("Circle area c = ", 3.14 * r3 **2)

def circle_area(r1,r2,r3):
    return r1 + r2 + r3
print(circle_area(314.0, 113.04, 50.24))
