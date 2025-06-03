class Bird:
    def fly(self):
        print('birds fly in the sky')
        
class Eagle(Bird):
    def fly(self):
        print('eagles fly at high altitude')
             
class Sparrow(Bird):
    def fly(self):
        print('sparow fly at a low altitude')
    
#How we use polymorphism
def flight_test(bird):
    bird.fly()
    
#creating objects
eagle1=Eagle()       
sparrow1=Sparrow()

#calling test_flight method
flight_test(eagle1)
flight_test(sparrow1)