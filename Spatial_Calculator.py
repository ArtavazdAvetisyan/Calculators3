import calculators.Calculator as Calculator


class Spatial_Calculator(Calculator.Calculator):

    def area(self, data):
        self.set_arguments(data)

        return self.width * self.length

    def volume(self, data):
        self.set_arguments(data)

        return self.width * self.length * self.height
