class Plane(object):

    flying_status = True

    def fly(self):
        self.flying_status = True

    def dont_fly(self):
        self.flying_status = False
