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

# Over all base class
class Vehicle:
    pass


# Base class for Starship and Airplane
class FlightVehicle(Vehicle):
    pass

class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass

# Base class for Car and MotorCycle
class GroundVehicle(Vehicle):
    pass

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass
