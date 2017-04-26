class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @property
    def nextdate(self):
        MONTH_30 = [4, 6, 9, 11]
        MONTH_31 = [1, 3, 5, 7, 8, 10, 12]

        if self.year < 1812 or self.year > 2016:
            return "INVALID"
        elif self.month < 1 or self.month > 12:
            return "INVALID"
        elif self.day < 1 or self.day > 31:
            return "INVALID"

        if self.month == 12 and self.day == 31:
            return self.text('y')
        elif self.month in MONTH_31 and self.day == 31:
            return self.text('m')
        elif self.month in MONTH_30 and self.day == 30:
            return self.text('m')
        elif not self.isleap and self.month == 2 and self.day == 28:
            return self.text('m')
        elif self.isleap and self.month == 2 and self.day == 29:
            return self.text('m')
        else:
            return self.text('d')

    @property
    def isleap(self):
        year = self.year
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return True
        else:
            return False

    def text(self, add):
        if add == 'y':
            return "%s, %s, %s" % (self.year + 1, 1, 1)
        elif add == 'm':
            return "%s, %s, %s" % (self.year, self.month + 1, 1)
        else:
            return "%s, %s, %s" % (self.year, self.month, self.day + 1)
