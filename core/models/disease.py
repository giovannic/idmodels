from core.expressions import Constant, Expression, Parameter
import numpy as np

class TemporalDiseaseModel():

    def __init__(self, population, dt):
        self._population = population
        self._dt = Constant(dt)
        self._transitions = list()
        self._parameters = list()

    @property
    def dt_expression(self):
        return self._dt

    @property
    def parameters(self):
        return self._parameters

    def set_number_of_simulations(n):
        self._population.set_number_of_simulations(n)

    def add_transition(self, x, y, exp):
        self._transitions.append((x, y, exp))

    def create_parameter(self, label):
        parameter = Parameter(label)
        self._parameters.append(parameter)
        return parameter

    def trace(self, steps, n):

        ''' initialises model expressions, runs n simulations and returns results'''

        # initialise expressions
        self._dt.initialise(n)
        self._population.initialise_expressions(n)
        for (x, y, exp) in self._transitions:
            exp.initialise(n)

        t = np.zeros(n)
        trace = list()
        trace.append(['t'] + self._population.compartment_labels)
        for _ in range(steps):
            trace.append([t.copy()[0]] + self._population.compartment_sizes)
            t += self._dt.value
            for x, y, exp in self._transitions:
                self._population.move(x, y, exp.evaluate())
        return trace
