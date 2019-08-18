from abc import ABC, abstractmethod
import numpy as np

class DeferredArithmeticMixin():

    def __mul__(self, other):
        return Multiply(self, other)

    def __truediv__(self, other):
        return Divide(self, other)

class BinaryExpressionMixin():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def initialise(self, n):
        self.x.initialise(n)
        self.y.initialise(n)

class Expression(ABC, DeferredArithmeticMixin):

    @abstractmethod
    def evaluate(self):
        '''Evaluates an expression, returns a float'''
        pass

    @abstractmethod
    def initialise(self, n):
        '''Initialises the the expression for the number of simulations'''
        pass

class Constant(Expression):

    def __init__(self, initial):
        self._initial = initial
        self._value = None

    @property
    def value(self):
        return self._value

    def evaluate(self):
        return self.value

    def initialise(self, n):
        self._value = np.full(n, self._initial)

class Variable(Expression):

    def __init__(self, initial):
        self._initial = initial

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value.copy()

    def evaluate(self):
        return self._value

    def initialise(self, n):
        self._value = np.full(n, self._initial)

class Parameter(Expression):

    '''A parameter is an expression whose value can set just before simulation time'''

    def __init__(self, label):
        self.label = label
        self._expression = None

    @property
    def expression(self):
        if self._expression is None:
            raise ValueError(
                'parameter {} needs to be set'.format(self.label)
            )
        return self._expression

    def set_value(self, value):
        self._expression = Constant(value)

    def evaluate(self):
        return self.expression.evaluate()

    def initialise(self, n):
        return self.expression.initialise(n)

class Divide(BinaryExpressionMixin, Expression):

    def evaluate(self):
        return self.x.evaluate() / self.y.evaluate()

class Multiply(BinaryExpressionMixin, Expression):

    def evaluate(self):
        return self.x.evaluate() * self.y.evaluate()

class Binomial(BinaryExpressionMixin, Expression):

    def evaluate(self):
        return np.random.binomial(self.x.evaluate(), self.y.evaluate())
