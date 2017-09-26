import calculators.Calculator as Calculator


class Conditioner_Calculator(Calculator.Calculator):

    def kwt(self, data):
        self.set_arguments(data)

        volume = self.width * self.length * self.height
        if self.units == 'f':
            volume *= 0.305 * 0.305 * 0.305;

        T1 = volume * self.insolation

        T2 = self.eq_power * 0.3 + self.illum_power

        T3 = self.people_num * 100

        return T1 + T2 + T3

    def btu(self, data):
        return self.kwt(data) / 0.2931
