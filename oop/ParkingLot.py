from collections import defaultdict

class Vehicle :
    def __init__(self, license, type, size):
        self.license = license
        self.type = type
        self.size = size
        self.spot = None
        self.level = None

    def can_fit(self, spot):
        pass

    def park(self, spot):
        self.spot = spot
        spot.available = False
        self.level = spot.level

    def unpark(self):
        if self.spot :
            parking = self.spot.parking
            parking.free(self, self.spot)
            self.spot = None


class Size :
    small, medium, large = 0, 1, 2

class Spot :
    def __init__(self, size):
        self.size = size
        self.available = False
        self.vehicle = None
        self.level = None
        self.parking = None

    def set_available(self):
        self.available = True

class Level :
    #spots = {"small":[], ...}
    def __init__(self, id, spots):
        self.id = id
        self.available_spots = self.initialize(spots)

    def initialize(self, spots):
        result = {}
        for size in spots :
            for spot in spots[size]:
                spot.level = self
            result[size] = spots[size]
        return result


    def find_spot(self, size):
        for possible_size in range(size, Size.large+1):
            if self.available_spots[possible_size]:
                spot = self.available_spots[possible_size].pop()
                return spot
        return None

    def add_spot(self, spot):
        self.available_spots[spot.size].append(spot)


class Parking:
    def __init__(self, levels):
        self.levels = levels
        self.vehicles = set([])


    def park(self, vehicle):
        size = vehicle.size
        curr_level = vehicle.level
        spot = self.available_parking_spot(curr_level, size)
        if spot :
            vehicle.park(spot)
        else:
            print("No available parking spot. Come later")

    def available_parking_spot(self, curr_level, size):
        idx = curr_level
        spot = self.levels[curr_level].find_spot(size) #look at current level
        for i in range(self.levels): #look at other levels
            if i == idx :
                continue
            if spot :
                break
            spot = self.levels[i].find_spot(size)
        return spot


    def unpark(self, vehicle):
        vehicle.unpark()

    def free(self, vehicle, spot):
        self.vehicles.remove(vehicle)
        spot.set_available()
        self.levels[spot.level].add_spot(spot)

    def parked_vehicles(self):
        return self.vehicles

