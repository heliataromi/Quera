from ground_vehicle import GroundVehicle
from flying_vehicle import FlyingVehicle



class Airplane(GroundVehicle, FlyingVehicle):
    def __init__(self, airline: str, number_of_crew: int, captain: str, **kwargs):
        self.airline = airline
        self.number_of_crew = number_of_crew
        self.captain = captain
        super().__init__(**kwargs)


class B707(Airplane):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
