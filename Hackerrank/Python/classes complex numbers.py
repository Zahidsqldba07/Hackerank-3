import math

class Complex(object):
	real = float()
	imaginary = float()

	def __init__(self,real,imaginary):                     
		self.real = real
		self.imaginary = imaginary

	def __add__(self,other):
		x = self.real + other.real
		y = self.imaginary + other.imaginary
		return Complex(x,y)

	def __sub__(self,other):
		x = self.real - other.real
		y = self.imaginary - other.imaginary
		return Complex(x,y)
	
	def __mul__(self,other):
		x = self.real*other.real - self.imaginary*other.imaginary
		y = self.imaginary*other.real + self.real*other.imaginary
		return Complex(x,y)

	def __truediv__(self,other):
		x = (self.real*other.real + self.imaginary*other.imaginary)/(other.real**2 + other.imaginary**2)
		y = (self.real*other.imaginary - self.imaginary*other.real)/(other.real**2 + other.imaginary**2)
		return Complex(x,-y)

	def mod(self):
		mod_num =  math.sqrt(self.real**2+self.imaginary**2)
		return Complex(mod_num,0)

	def __str__(self):
		if self.imaginary == 0:
			result = "%.2f+0.00i" %(self.real)
		elif self.real == 0:
			if self.imaginary >= 0 :
				result = "0.00+%.2fi" %(self.imaginary)
			elif self.imaginary < 0 :
				result = "0.00-%.2fi" %(abs(self.imaginary))

		elif self.imaginary > 0:
			result = "%.2f+%.2fi" % (self.real, self.imaginary)
		else:
			result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
		return result

cr,ci = input().split(' ')
dr,di = input().split(' ')
cr = float(cr)
ci = float(ci)
dr = float(dr)
di = float(di)
C = Complex(cr,ci)
D = Complex(dr,di)

Sum = C + D 
Sub = C - D
Prod = C * D
Div = C / D

print(Sum)
print(Sub)
print(Prod)
print(Div)
print(C.mod())
print(D.mod())