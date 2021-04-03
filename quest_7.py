class Complex():

    def __init__(self, Re, Im):
        self.Re = Re
        self.Im = Im

    def __str__(self):
        if self.Im >= 0:
            return f"{self.Re} + {self.Im}i"
        else:
            return f"{self.Re} - {abs(self.Im)}i"

    def __add__(self, other):
        return Complex(self.Re + other.Re, self.Im + other.Im)

    def __mul__(self, other):
        return Complex(self.Re * other.Re - self.Im * other.Im, self.Re * other.Im + self.Im * other.Re)


a_1 = Complex(5, -4)
a_2 = Complex(3, 2)
print(a_1, a_2)
print(a_1 + a_2)
print(a_1 * a_2)
