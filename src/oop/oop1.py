# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#Vehicle Class
class Vehicle():
    pass

#FlgithVehicle Class
class FlightVehicle(Vehicle):
    pass

#Starship Class
class Starship(FlightVehicle):
    pass

#GroundVehicle Class
class GroundVehicle(Vehicle):
    pass

#Airplane Class
class Airplane(FlightVehicle):
    pass

#Car Class
class Car(GroundVehicle):
    pass

#Motorcycle Class
class Motorcycle(GroundVehicle):
    pass