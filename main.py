class Human:
    def __init__(self, name='Human'):
        self.name = name

class Auto:
    def __init__(self, brand, сapacity):
        self.brand = brand
        self.сapacity = сapacity
        self.passengers = []

    def add_passenger(self, human):
        if len(self.passengers) < self.сapacity:
            self.passengers.append(human)
        else:
            print('there are no free seats')

    def print_all_passenger(self):
        if self.passengers != []:
            print(f"There are {len(self.passengers)} passengers in {self.brand}")
            for pas in self.passengers:
                print(pas.name)
        else:
            print(f'no passengers in {self.brand}')

class Wheels:
    def __init__(self,):
        self.wheels = wheels

    def print_wheels(self):
        if self.wheels:
            print(f"There are {len(self.wheels)} Wheels in {self.brand}")



