class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name.title()} {self.age}"

    def __del__(self):
        print("Object is being deconstructed!")

man = Person("mike", 21)
# print(man)
# del man

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"X = {self.x}\nY = {self.y}"

    def __call__(self):
        print("Hello I was called!")


    def __len__(self):
        return 10


vector1 = Vector(10, 20)
vector2 = Vector(40, 50)
vector3 = vector1 + vector2
# print(vector3)
# print(len(vector3))

# vector3()






if __name__ == '__main__':
    pass
