
from cars import Cars
class Junction:
    def __init__(self):

        self.num_paths_in = 0
        self.cars_in_streets = {}  # holds
        self.num_cars = 0
        self.used_streets = set()
        self.used = False
    def add_path(self, street):

        self.num_paths_in += 1
        self.cars_in_streets[street] = []
        self.times_used = 0
    def add_car(self, car):
        self.cars_in_streets[car.current_street].append(car.num)
        self.num_cars += 1

    def remove_car(self,car):

        self.cars_in_streets[car.current_street].pop(0)
        self.num_cars -= 1
        self.used = True
        self.times_used += 1
    def compare_cars(self, cars):
        # determines which car should go first
        best_car = 0
        minimum_time = float("inf")

        for car_list in self.cars_in_streets.values():
            # compare the first cars in the intersections

            if len(car_list) > 0:
                car = car_list[0]
                car_value = cars[car].time_required
                if car_value < minimum_time:
                    best_car = car
                    minimum_time = car_value


        return best_car