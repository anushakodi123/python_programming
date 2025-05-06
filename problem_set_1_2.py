class JobProfessional:
    def __init__(self, yearly_income, portion_saved, cost_of_dream_home, portion_down_payment, r, semi_annual_rise):
        self.amount_saved = 0
        self.yearly_income = yearly_income
        self.portion_saved = portion_saved
        self.cost_of_dream_home = cost_of_dream_home
        self.portion_down_payment = portion_down_payment
        self.r = r
        self.semi_annual_rise = semi_annual_rise

    def calculate_no_of_months(self):
        months = 0
        to_be_paid_for_house = self.portion_down_payment * self.cost_of_dream_home
        monthly_income = self.yearly_income / 12

        while self.amount_saved < to_be_paid_for_house:
            interest = self.amount_saved * (self.r / 12)
            monthly_saving = self.portion_saved * monthly_income
            self.amount_saved += interest + monthly_saving
            months += 1
            if months%6 == 0:
                self.yearly_income += self.yearly_income * semi_annual_rise
                monthly_income = self.yearly_income / 12

        return months


yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_rise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25
r = 0.05

j = JobProfessional(yearly_salary, portion_saved, cost_of_dream_home, portion_down_payment, r, semi_annual_rise)
print("Number of months:", j.calculate_no_of_months())
