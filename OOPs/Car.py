class Car:
    total_car = 0  #Class Variable
    def __init__(self, __brand,model): #Encapsulation
        self.__brand = __brand  #__ makes an attribute private making it accessible only inside the class and 
                                #can be accesed outside class using getter method(Encapsulation)
        self.__model = model
        Car.total_car +=1
    
    def get_brand(self):
        return self.__brand+"!" 
    
    def fuel_type(self):
        return "Petrol or diesel"

    def full_name(self):
        return f"{self.__brand} {self.__model}" #formatting String
    
    @staticmethod
    def gen_description():
        return "Cars are means of Transport"
    
    @property
    def model(self):
        return self.__model
class Electric_car(Car):  #Inheritance
    def __init__(self,__brand,__model, battery_size):
        super().__init__(__brand,__model)
        self.battery_size = battery_size
    
    def fuel_type(self):  #Polymorphism
        return "Electric charge"
        


my_car = Car("Toyota","Innova")
# print(my_car.get_brand)
# print(my_car.full_name())
# print(my_car.get_brand())
# print(my_car.fuel_type())
# print(Electric_car("Tesla","Cybertruck","85kWh").fuel_type())
# print(Car.total_car)
# print(my_car.model)
print(isinstance(my_car,Car)) # to check wether the object belongs to a class



# In Python, __init__ is a special method (constructor) used in classes to initialize object attributes 
# when an instance of the class is created.

# In Python, self is a reference to the current instance of a class.
# It allows access to instance attributes and methods within the class.

# Static method : Methods which is accessible through class only rather than its instances.
# Multiple inheritance is allowed in python