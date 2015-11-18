import random

class Weather(object):
    weather_options = ['sunny','sunny','sunny','sunny','stormy']

    def weather_rand(self):
        return self.weather_options[random.randint(0,4)]
