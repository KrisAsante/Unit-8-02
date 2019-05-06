# Created by: Chris Asante
# Created on: 6-May-2019
# Created for: ICS3U
# Unit 8-02
# This main program will create a car object

from car import *

#create a vehicle
car1 = Car()
car2 = Car()

print("Speed: " + str(car1.speed))
car1.accelerate(100)
print("Speed: " + str(car1.speed))
car1.license_plate_number = "QWE123R4"
print("License plate number: " + str(car1.license_plate_number) + '\n')

print("Speed: " + str(car2.speed))
car2.accelerate(50)
print("Speed: " + str(car2.speed))
car2.brake(70)
print("Speed: " + str(car2.speed))
car2.colour = "blue"
print("Colour: " + str(car2.colour))