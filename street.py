START = 0
END = 1
NAME = 2
TIME = -1
class Street:
    def __init__(self):
        self.time_to_cross = 0
        self.start = 0
        self.end = 0
        self.name = ""
        self.times_used = 0
    def street_creator(self, details):

        self.start = int(details[START])
        self.end =int(details[END])
        self.time_to_cross = int(details[TIME])
        self.name = details[NAME]