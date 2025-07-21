from vehicle import Vehicle


class FlyingVehicle(Vehicle):
    def __init__(self, fuel: str, number_of_fins: int, **kwargs):
        self.fuel = fuel
        self.number_of_fins = number_of_fins
        super().__init__(**kwargs)
