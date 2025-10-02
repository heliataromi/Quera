import unittest 
from main import Trip, Passenger, Train


class TestTrip(unittest.TestCase):

    def test_call(self):
        train = Train(last_visited_city='Sanandaj', weight_capacity=34286, is_on_trip=False)
        passenger1 = Passenger(fullname='Ali Saeedi', load_weight=616)
        passenger2 = Passenger(fullname='Abolfazl Zandi', load_weight=349)
        trip = Trip(origin_city='Sanandaj', destination_city='Rasht', train=train)

        self.assertEqual(trip(), 34286, '\nتابع __call__ را به درستی پیاده‌سازی نکرده‌اید.')

        trip.passengers = [passenger1]
        self.assertEqual(trip(), 34286 - 616, '\nتابع __call__ را به درستی پیاده‌سازی نکرده‌اید.')

        trip.passengers = [passenger1, passenger2]
        self.assertEqual(trip(), 34286 - 616 - 349, '\nتابع __call__ را به درستی پیاده‌سازی نکرده‌اید.')


class TestPassenger(unittest.TestCase):

    def test_str(self):
        passenger1 = Passenger(fullname='Ali Saeedi', load_weight=616)
        self.assertEqual(str(passenger1), 'Ali Saeedi', '\n تابع __str__ را به درستی پیاده‌سازی نکرده‌اید.')


if __name__ == '__main__':
    unittest.main()