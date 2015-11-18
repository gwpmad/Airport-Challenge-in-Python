from plane import Plane
from weather import Weather

class Airport(object):

    DEFAULT_CAPACITY = 50
    weather = 'sunny'
    planes = []


    def __init__(self, capacity=None):
        if capacity == None:
            self.capacity = Airport.DEFAULT_CAPACITY #use Airport rather than self here because the self hasn't been instantiated yet
        elif type(capacity) != int: #rather than just capacity != int - you can't do that because capacity itself won't return int, which is what we're testing!
            raise ValueError('the capacity entered is not an integer')
        else:
            self.capacity = capacity

    def weather_report(self,weather_klass):
        return weather_klass.weather_rand
        return 'sunny'

    def plane_land(self,plane):
        if self.weather_report(Weather()) == 'stormy':
            raise Exception('weather is stormy')
        elif self.is_full_capacity == True:
            raise Exception('airport is full')
        elif plane in self.planes: #python equivalent of .include?
            raise Exception('this plane already in this airport')
        else:
            plane.dont_fly()
            self.planes.append(plane)

    def plane_take_off(self,plane):
        if self.weather_report == 'stormy':
            raise Exception('weather is stormy')
        elif len(self.planes) == 0:
            raise Exception('there are no planes')
        elif self.planes[self.planes.index(plane)] == True:
            raise Exception('a flying plane can\'t take off')
        else:
            plane.fly()
            self.planes.remove(plane)


    def is_full_capacity(self):
        if len(self.planes) == self.capacity:
            return True
        else:
            return False
