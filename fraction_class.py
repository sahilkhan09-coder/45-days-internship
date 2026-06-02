from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator


    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        num = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        den = self.denominator * other.denominator

        common = gcd(num, den)
        return Fraction(num // common, den // common)

  
    def __eq__(self, other):
        return (self.numerator * other.denominator ==
                other.numerator * self.denominator)

  
    def __lt__(self, other):
        return (self.numerator * other.denominator <
                other.numerator * self.denominator)


f1 = Fraction(1, 2)
f2 = Fraction(1, 3)

print("Fraction 1:", f1)
print("Fraction 2:", f2)
print("Addition:", f1 + f2)
print("Equal:", f1 == f2)
print("Less Than:", f1 < f2)

print("-" * 30)

f3 = Fraction(2, 4)
f4 = Fraction(1, 2)

print("Fraction 3:", f3)
print("Fraction 4:", f4)
print("Addition:", f3 + f4)
print("Equal:", f3 == f4)
print("Less Than:", f3 < f4)

print("-" * 30)

f5 = Fraction(3, 5)
f6 = Fraction(4, 5)

print("Fraction 5:", f5)
print("Fraction 6:", f6)
print("Addition:", f5 + f6)
print("Equal:", f5 == f6)
print("Less Than:", f5 < f6)
