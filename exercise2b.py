class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if (self.dr < 0):
            self.nr = self.nr * -1
            self.dr = self.dr * -1
        else:
            None

    def show(self):
        print(self.nr, "/", self.dr)

    def multiply(self, frac2):
        if type(frac2) == int:
            return Fraction(self.nr * frac2, self.dr)
        else:
            return Fraction(self.nr * frac2.nr, self.dr * frac2.dr)

    def add(self, frac2):
        if type(frac2) == int:
            return Fraction(self.nr + self.dr * frac2, self.dr)
        else:
            return Fraction(self.nr * frac2.dr + self.dr * frac2.nr, self.dr * frac2.dr)



f1 = Fraction(2,3)
f1.show()
f2 = Fraction(3,4)
f2.show()
f3 = f1.multiply(f2)
f3.show()
f3 = f1.add(f2)
f3.show()
f3 = f1.add(5)
f3.show()
f3 = f1.multiply(5)
f3.show()