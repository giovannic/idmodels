from core.expressions import Variable, Constant, Parameter
import numpy as np

class FixedPopulationModel():

    def __init__(self):
        self._size = 0
        self._compartments = list()
        self._size_expression = Parameter('population_size')
        self._simulation_size = 1

    @property
    def size(self):
        return self._size_expression

    @property
    def compartment_sizes(self):
        return [
            size
            for compartment in self._compartments
            for size in compartment.size.evaluate()
        ]

    @property
    def compartment_labels(self):
        if self._simulation_size == 1:
            return [
                compartment.label for compartment in self._compartments
            ]
        else:
            return [
                '{}_{}'.format(compartment.label, i)
                for compartment in self._compartments
                for i in range(self._simulation_size)
            ]

    def initialise_expressions(self, n):
        self._simulation_size = n
        for compartment in self._compartments:
            compartment.initialise(n)
        self._size_expression.set_value(self._size)
        self._size_expression.initialise(n)

    def create_compartment(self, label, initial=0):
        self._size += initial
        if initial < 0:
            raise ValueError('populations must be positive')
        compartment = self.Compartment(label, initial)
        self._compartments.append(compartment)
        return compartment

    def move(self, x, y, n):
        shift = np.minimum(x.size.value, n)
        x.size.value -= shift
        y.size.value += shift

    class Compartment():

        def __init__(self, label, initial):
            self.label = label
            self._size = Variable(initial)

        @property
        def size(self):
            return self._size

        def initialise(self, n):
            self._size.initialise(n)
