class Car:
    def __init__(self):
        self.name = ""
        self.manufacturer = ""
        self.year = 0
        self.description = ""
    def info(self):
        print(f"Car name: {self.manufacturer} {self.name}")
        print(f"Description: {self.description}")
        print(f"Year released: {self.year}")

    def set_details(self, year, description):
        self.year = year
        self.description = description

all_cars = []

car1  = Car()
car1.name = "M3 GTR"
car1.manufacturer = "BMW"
car1.set_details(2001, "Best car in NFS Most Wanted")
all_cars.append(car1)

car2 = Car()
car2.name = "RX-8"
car2.manufacturer = "BMW"
car2.set_details(2002, "Best car in NFS Underground 2")
all_cars.append(car2)

car3 = Car()
car3.name = "Le Mans Quattro"
car3.manufacturer = "Audi"
car3.set_details(2003, "Best car in NFS Carbon")
all_cars.append(car3)

for c in all_cars:
    c.info()
    print()