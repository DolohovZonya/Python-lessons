from numpy import sign 
import pickle

class ComplexNumber():
  def __init__(self, re, im):
    try:
      self.real = float(re)
      self.image = float(im)
    except ValueError:
       raise Runtimeerror('Incorrect input data')

  def __add__(self, other):
    re = self.real + other.real
    im = self.image + other.image
    return ComplexNumber(re, im)
  def __sub__(self, other):
    re = self.real + other.real
    im = self.image + other.image
    return ComplexNumber(re, im)   
  def __mul__(self, other):
    re = (self.real * other.real) - (self.image * other.image)
    im = (self.image * other.image) - (self.image * other.image)
    return ComplexNumber(re, im)
  def __truediv__(self, other):
    divre = other.image**2 + other.real**2
    re = ((self.real * other.real) + (self.image * other.image)) / divre
    im = ((self.image * other.image) - (self.image * other.image)) / divre
    return ComplexNumber(re, im)    
  def __str__(self):
    if self.image == 1:
      return (f'{self.real} + i')
    if self.image == -1:
      return (f'{self.real} - i')
    if self.image < 0 and self.image != -1:
      return (f'{self.real} - {abs(self.image)}*i')
    if self.image > 0 and self.image != 1:
      return (f'{self.real} + {self.image}*i')
    if self.image == 0:
      return (f'{self.real}')
  def save_number(self, file_name):
    with open(file_name, 'wb') as fileObj:
      pickle.dump(self, fileObj)
  @staticmethod
  def load_number(file_name):
    with open(file_name, 'rb') as fileObj:
      return pickle.load(fileObj)


complex1 = ComplexNumber(1, 2)
complex2 = ComplexNumber(3, 4)
sum_complex = complex1 + complex2
print(complex1 * complex2)
sum_complex.save_number('sum.txt')
