### Thomas Silva
### ENGR 103 Project 5b.


class Taxicab:
## creates the clas
### Initialize x and y coordinates and the odometer to the given values ###
    def __init__(self, x=0, y=0):
        self.x_coord = x
        self.y_coord = y
        self.odometer = 0

    def get_x_coord(self):
        return self.x_coord

    def get_y_coord(self):
        return self.y_coord

    def get_odometer(self):
        return self.odometer
# Moves the taxi in the x and y directions according to the given value ###
    def move_x(self, distance):
        self.x_coord += distance
        self.odometer += abs(distance)

    def move_y(self, distance):
        self.y_coord += distance
        self.odometer += abs(distance)

### Example: ###
cab = Taxicab()
cab.move_x(5)
cab.move_y(3)
print(f"Current position: ({cab.get_x_coord()}, {cab.get_y_coord()})")
print(f"Odometer reading: {cab.get_odometer()}")

