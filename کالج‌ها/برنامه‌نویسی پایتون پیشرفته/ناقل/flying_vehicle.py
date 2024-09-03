from vehicle import Vehicle


class FlyingVehicle(Vehicle):
    def __init__(self, fuel, number_of_fins, **kwargs):
        self.fuel = fuel
        self.number_of_fins = number_of_fins
        super().__init__(**kwargs)
