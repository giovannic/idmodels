from abc import ABC, abstractmethod
import numpy as np

class DeferredArithmetic():

    def __mul__(self, other):
        return Multiply(self, other)

    def __truediv__(self, other):
        return Divide(self, other)

class Expression(ABC, DeferredArithmetic):

    @abstractmethod
    def evaluate():
        '''Evaluates an expression, returns a float'''
        pass

class Constant(Expression):

    def __init__(self, value):
        if value is None:
            raise ValueError('Constants must be numeric')
        self._value = value

    @property
    def value(self):
        return self._value

    def evaluate(self):
        return self.value

class Variable(Expression):

    def __init__(self, value):
        if value is None:
            raise ValueError('Variables must be numeric')
        self.value = value

    def evaluate(self):
        return self.value

class Divide(Expression):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def evaluate(self):
        return self.x.evaluate() / self.y.evaluate()

class Multiply(Expression, DeferredArithmetic):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def evaluate(self):
        return self.x.evaluate() * self.y.evaluate()

class Binomial(Expression):

    def __init__(self, n, p):
        self.n = n
        self.p = p

    def evaluate(self):
        return np.random.binomial(self.n.evaluate(), self.p.evaluate())
