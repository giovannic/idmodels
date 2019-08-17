from core.expressions import Constant, Expression

class TemporalDiseaseModel():

    def __init__(self, population, dt):
        self._population = population
        self._dt = Constant(dt)
        self.t = 0
        self._transitions = list()
        self._parameters = list()

    @property
    def dt_expression(self):
        return self._dt

    @property
    def parameters(self):
        return self._parameters

    def add_transition(self, x, y, exp):
        self._transitions.append((x, y, exp))

    def create_parameter(self, label):
        parameter = self.Parameter(label)
        self._parameters.append(parameter)
        return parameter

    def step(self):
        self.t += self._dt.value
        for x, y, exp in self._transitions:
            self._population.move(x, y, exp.evaluate())

    def trace(self, steps):
        trace = list()
        trace.append(['t'] + self._population.compartment_labels)
        for _ in range(steps):
            trace.append([self.t] + self._population.compartment_sizes)
            self.step()
        return trace

    class Parameter(Expression):

        '''A parameter is an expression that can be set just before runtime'''

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
