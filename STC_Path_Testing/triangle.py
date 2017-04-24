class triangle(object):
    def __init__(self, a, b, c):
        self.edges = [a, b, c]

    @property
    def type(self):
        def c1(x):
            return x[0] + x[1] <= x[2]

        def c2(x):
            return x[0] == x[1] == x[2]

        def c3(x):
            return x[0] ** 2 + x[1] ** 2 == x[2] ** 2

        def c4(x):
            return (x[0] != x[1] == x[2]) or (x[0] == x[1] != x[2])

        for edge in self.edges:
            if edge <= 0 or edge > 200:
                return "NOT TRIANGLE"

        for i in range(3):
            if c1(self.edges[i:] + self.edges[:i]):
                return "NOT TRIANGLE"

        if c2(self.edges):
            return "EQUALATERAL"

        self.edges.sort()

        if c3(self.edges):
            return "RIGHT TRIANGLE"

        if c4(self.edges):
            return "ISOSCELES"

        return "SCALENE"
