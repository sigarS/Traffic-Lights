from street import Street

class Cars:
    def __init__(self):
        self.path = []
        self.time_required = 0
        self.destination = False
        self.path_length = 0
        self.num = 0
        self.current_intersection = 0
        self.current_street = ""

    def car_creator(self, details, streets):
        details.strip().split(" ")
        self.path_length = int(details[0])
        self.path = details.split(" ")[1:]
        self.destination = self.path[-1]

        self.current_intersection = streets[self.path[0]].end
        self.current_street = self.path[0]
        streets[self.path[0]].times_used += 1

    def next_road(self, street):
        self.time_required -= street[self.path[0]].time_to_cross
        self.path.pop(0)
        self.path_length -= 1
        self.current_street = self.path[0]


        street[self.path[0]].times_used += 1
        self.current_intersection = street[self.current_street].end # make sure car is added to the intersection at the right time
