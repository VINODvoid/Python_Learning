class Car:
    def __init__(self ,brand,model):
        self.__brand = brand
        self.model = model
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return self.__brand + " FY-24"

class ElectricCar(Car) : #Inheritance
    def __init__(self,brand,model,battery_size):
        self.battery_size = battery_size
        super().__init__(brand,model)


# my_car = Car("Toyota","Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Ford","Mustang")
# print(my_new_car.brand)
# print(my_new_car.model)
# print(my_new_car.full_name())

my_electric_car = ElectricCar("Tesla","Model 3",75)
# print(my_electric_car.__brand) # ! Error saying __brand is private
print(my_electric_car.model)
print(my_electric_car.full_name())
print(my_electric_car.battery_size)
print(my_electric_car.get_brand())


