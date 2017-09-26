import calculators.Calculator as Calculator


class Financial_Calculator(Calculator.Calculator):

    def annuity_payments(self, data):
        self.set_arguments(data)

        rate = self.interest / 1200
        payment = self.principal * (rate + rate / (pow(1 + rate, self.period) - 1))

        return [payment, payment * self.period]

    def differentiated_payments(self, data):
        self.set_arguments(data)

        payments = dict()

        main_payment = self.principal / self.period

        total = 0

        for n in range(0, self.period):
            debt_remained = self.principal - (main_payment * n)
            added_interest = debt_remained * self.interest / 100 / 12
            payments[n] = main_payment + added_interest
            total += payments[n]

        return [payments, total]

    def simple_interest(self, data):
        self.set_arguments(data)

        income =  self.principal * (1 + self.interest /100 * self.period / self.days_in_year)
        return income * (1 - self.tax / 100);

    def compound_interest(self, data):
        self.set_arguments(data)

        income =  self.principal * (1 + self.interest /100 / self.annual_periods) ** self.total_periods
        return income * (1 - self.tax / 100);
