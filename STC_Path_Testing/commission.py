class Commission(object):
    def __init__(self, locks, stocks, barrels):
        self.locks = locks
        self.stocks = stocks
        self.barrels = barrels

    @property
    def bonus(self):
        if self.locks == -1:
            return "Terminate"

        if self.locks < 1 or self.locks > 70:
            return "Invalid"
        elif self.stocks < 1 or self.stocks > 80:
            return "Invalid"
        elif self.barrels < 1 or self.barrels > 90:
            return "Invalid"

        sales = self.locks * 45 + self.stocks * 30 + self.barrels * 25

        if sales >= 1800:
            return 220 + 0.2 * (sales - 1800)
        elif sales >= 1000:
            return 100 + 0.15 * (sales - 1000)
        else:
            return 0.1 * sales