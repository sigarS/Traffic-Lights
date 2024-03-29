from cars import Cars
from street import Street
from junction import Junction
from collections import defaultdict
import numpy as np
STREET_NAME = 2

def main(filename):

    file = open(filename + ".txt", "r")

    content = file.read().strip().split('\n')
    file.close()

    simulation_time, num_intersection, num_streets, num_cars, reward = content[0].strip().split(" ")
    simulation_time, num_intersection, num_streets, num_cars, reward = \
        int(simulation_time), int(num_intersection), int(num_streets), int(num_cars), int(reward)

    streets = {}
    intersections = {}
    intersections_count = 0
    intersections_added = []
    intersection_change = [] # list of all intersection that have more than two roads going in.
    for street in content[1: num_streets + 1]:
        # creating a dictionary of all the streets

        temp_street = street.strip().split(" ")
        street_name = temp_street[STREET_NAME]
        streets[street_name] = Street()
        streets[street_name].street_creator(temp_street)

        # add intersection number and streets
        intersection_id = streets[street_name].end

        if intersections_count < num_intersection and intersection_id not in intersections_added:

            intersections[intersection_id] = Junction()
            intersections[intersection_id].add_path(street_name)
            intersections_added.append(intersection_id)
        else:

            intersections[intersection_id].add_path(street_name)


    cars_paths = content[num_streets + 1:]
    cars = {}

    for i in range(num_cars):
        # create car class and add cars to intersections
        cars[i] = Cars()
        #print(cars_paths[i])
        cars[i].car_creator(cars_paths[i], streets)
        cars[i].num = i
        intersections[cars[i].current_intersection].add_car(cars[i])

        if cars[i].current_intersection not in intersection_change:
            intersection_change.append(cars[i].current_intersection)

    time_add_car = {} #dictionary that holds the time at which a car should be added.
    intersection_used = set()# holds a set of all intersections used
    for time in range(simulation_time):

        end = len(intersection_change)
        i = 0

        while i < end:

            junction = intersection_change[i]
            intersection_used.add(junction)

            car_moved = cars[intersections[junction].compare_cars(cars)].num


            intersections[junction].remove_car(cars[car_moved])


            if intersections[junction].num_cars == 0:
                # removing car and shrinking the num of iteration required
                intersection_change.remove(junction)
                i -= 1
                end -= 1


            cars[car_moved].next_road(streets)
            # car has reached its destination
            if cars[car_moved].path[0] == cars[car_moved].destination:
                pass
            else:
                # gets time to add car to a certain intersection and the car to be added

                time_to_add = streets[cars[car_moved].current_street].time_to_cross + time

                if time_to_add in time_add_car.keys():
                    time_add_car[time_to_add].append(car_moved)
                else:
                    time_add_car[time_to_add] = [car_moved]
            i += 1
        if time in time_add_car.keys():
            # convert this to use default dict
            for car in time_add_car[time]:
                intersections[cars[car].current_intersection].add_car(cars[car])
                if cars[car].current_intersection not in intersection_change:
                    intersection_change.append(cars[car].current_intersection)
    document = open(filename + " ans.txt", "w")
    document.write( f"{len(intersection_used)}\n")
    for intersection, inter_class in intersections.items():

        count = 0
        ans = ""
        if inter_class.used:
            document.write(f"{intersection}\n")
            if inter_class.num_paths_in == 1:
                document.write(f"1\n{list(inter_class.cars_in_streets.keys())[0]} 1\n")
                pass
            else:
                for street in inter_class.cars_in_streets:

                    if streets[street].times_used != 0:
                        count += 1
                        seconds_on = max(round(inter_class.num_paths_in * streets[street].times_used/inter_class.times_used), 1)
                        ans += f"{street} {seconds_on}\n"

                if count != 0:

                    document.write(f"{count}\n{ans}")

if __name__ == '__main__':
    main()