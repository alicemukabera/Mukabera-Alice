from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def star(self):
        pass
class Car(Vehicle):
     def star(self):
         print('kikikikinnmm, vuum, vumm,vuuummm...')   
         
         
class  Bike(Vehicle):
     def star(self):
         print('kikikikinnmm, ndrinn, ndrinnn,ndrinn...')   
bike1=Bike()
car1=Car() 
bike1.star()
car1.star()
 

                