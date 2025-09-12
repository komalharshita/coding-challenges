class Car:
    manufacturer = "Lamborghini" 
    build_date = 2020 
huracan = Car()

print(huracan.manufacturer)

class Sport:
    type = "Football"

class Person:
    name = "Bob"

bob = Person()
print(bob.name)

class Point:
    x = 0
    y = 0
    def update_x(self, new_x):
        self.x = new_x
    def update_y(self, new_y):
        self.y = new_y

