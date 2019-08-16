from core.expressions import Variable, Constant

class FixedPopulation():

    def __init__(self):
        self._size = 0
        self.compartments = list()

    @property
    def size(self):
        return Constant(self._size)

    def create_compartment(self, label, initial=0):
        self._size += initial
        if initial < 0:
            raise ValueError('populations must be positive')
        compartment = self.Compartment(label, initial)
        self.compartments.append(compartment)
        return compartment

    def move(self, x, y, n):
        if n < 0:
            return move(y, x, -n)
        if x.size.value < n:
            shift = x.size.value
        else:
            shift = n
        x.size.value -= shift
        y.size.value += shift

    class Compartment():

        def __init__(self, label, initial):
            self.label = label
            self._size = Variable(initial)

        @property
        def size(self):
            return self._size
