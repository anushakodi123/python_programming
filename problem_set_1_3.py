class JobProfessional:
    def __init__(self, deposit_amount):
        self.deposit_amount = deposit_amount
        self.cost_of_house = 800000
        self.down_payment = 25 / 100

    def calculate_rate_of_intrest(self):
        target = self.cost_of_house * self.down_payment
        max_possible = self.deposit_amount * ((1 + 1/12) ** 36)

        if self.deposit_amount >= target - 100:
            print("Best savings rate: 0.0")
            print("Steps in bisection search: 0")
            return 0.0

        if max_possible < target - 100:
            print("It is not possible to reach the down payment in 3 years.")
            return None

        amount = 0
        count = 0
        r1 = 0.0
        r2 = 1.0
        r = 0.0

        while abs(amount - target) > 100:
            r = (r1 + r2) / 2
            amount = self.deposit_amount * ((1 + (r / 12)) ** 36)

            if amount > target:
                r2 = r
            else:
                r1 = r

            count += 1

        print(f"Best savings rate: {r}")
        print(f"Steps in bisection search: {count}")
        return r

j = JobProfessional(65000)
j.calculate_rate_of_intrest()
