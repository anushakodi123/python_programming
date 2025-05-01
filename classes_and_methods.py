class Date:
    month_obj = {
            'January': 1,
            'February': 2,
            'March': 3,
            'April': 4,
            'May': 5,
            'June': 6,
            'July': 7,
            'August': 8,
            'September': 9,
            'October': 10,
            'November': 11,
            'December': 12      
        }
    def __init__(self, month, date, year):
        self.year = year
        self.month = Date.month_obj[month]
        self.date = date

    def __str__(self):
        return f'{self.year}-{self.month:02d}-{self.date:02d}'
    
    def is_after(self, other):
        month, date, year = other
        month = Date.month_obj[month]
        if year > self.year:
            return True
        if self.year == year and month > self.month:
            return True
        if self.year == year and self.month == month and date > self.date:
            return True
        return False
date = Date('June', 22, 1933)
print(date.is_after(('May', 17, 1933)))

    