from vehicle import Vehicle


class GroundVehicle(Vehicle):
    def __init__(self, number_of_wheels: int, steering_wheel: str, **kwargs):
        self.number_of_wheels = number_of_wheels
        self.steering_wheel = steering_wheel
        super().__init__(**kwargs)
