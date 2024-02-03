
#######################ex 1################################

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def __eq__(self, other):
        return self.radius == other.radius
    def __lt__(self, other):
        return self.radius*3.14*2 < other.radius*3.14*2
    def __gt__(self, other):
        return self.radius*3.14*2 > other.radius*3.14*2
    def __le__(self, other):
        return self.radius*3.14*2 <= other.radius*3.14*2
    def __ge__(self, other):
        return self.radius*3.14*2 >= other.radius*3.14*2
    def __add__(self, other):
        return self.radius + other.radius
    def __sub__(self, other):
        return self.radius - other.radius    
    def __iadd__(self, other):
        self.radius += other
        return self.radius
    def __isub__(self, other):
        self.radius -= other
        return self.radius


c1= Circle(10)
c2= Circle(15)
print(c1==c2)
print(c1<c2)
print(c1>c2)
print(c1<=c2)
print(c1>=c2)
print(c1+c2)
print(c1-c2)
c1 += 5
print(c1)
c2 -= 5
print(c2)



#######################ex 2################################

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real_part, imag_part)
    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"



c1 = Complex(2, 3)
c2 = Complex(1, -1)


print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)




#######################ex 3################################

class Airplane:
    def __init__(self, type_of_airplane, max_passengers, passengers):
        self.type_of_airplane = type_of_airplane
        self.passengers = passengers
        self.max_passengers = max_passengers
    def __eq__(self, other):
        return self.type_of_airplane == other.type_of_airplane
    def __lt__(self, other):
        return self.max_passengers < other.max_passengers
    def __gt__(self, other):
        return self.max_passengers > other.max_passengers
    def __le__(self, other):
        return self.max_passengers <= other.max_passengers
    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers
    def __add__(self, other):
        return self.passengers + other.passengers
    def __sub__(self, other):
        return self.passengers - other.passengers    
    def __iadd__(self, other):
        self.passengers += other
        return self.passengers
    def __isub__(self, other):
        self.passengers -= other
        return self.passengers


a1= Airplane("Гражданский", 235, 204)
a2= Airplane("Военный", 106, 98)
print(a1==a2)
print(a1<a2)
print(a1>a2)
print(a1<=a2)
print(a1>=a2)
print(a1+a2)
print(a1-a2)
a1 += 5
print(a1)
a2 -= 5
print(a2)






#######################ex 4################################

class Flat:
    def __init__(self, square, price):
        self.square = square
        self.price = price
    def __eq__(self, other):
        return self.square == other.square
    def __lt__(self, other):
        return self.price < other.price
    def __gt__(self, other):
        return self.price > other.price
    def __le__(self, other):
        return self.price <= other.price
    def __ge__(self, other):
        return self.price >= other.price
    def __ne__(self, other):
        return self.square != other.square


f1= Flat(60, 15000000)
f2= Flat(75, 20000000)
print(f1==f2)
print(f1!=f2)
print(f1<f2)
print(f1>f2)
print(f1<=f2)
print(f1>=f2)

