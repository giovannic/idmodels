from core.models import IDModel
from core.population import FixedPopulation
import unittest

class IDMTestCase(unittest.TestCase):

    def test_will_update_population_on_timestep(self):
        population = FixedPopulation()
        susceptable = population.create_compartment('susceptable', initial=1000)
        infected = population.create_compartment('infected', initial=1)
        model.set_population(population)
        model.add_transition(susceptable, infected, Constant(1))
        model.step(1)
        self.assertEquals(susceptable.size.value, 999)
        self.assertEquals(infected.size.value, 2)

    def test_will_update_population_on_timestep_multiple_transitions(self):
        population = FixedPopulation()
        susceptable = population.create_compartment('susceptable', initial=1000)
        infected = population.create_compartment('infected', initial=1)
        recovered = population.create_compartment('recovered')
        model.set_population(population)
        model.add_transition(susceptable, infected, Constant(1))
        model.add_transition(infected, recovery, Constant(1))
        model.step(1)
        self.assertEquals(susceptable.size.value, 999)
        self.assertEquals(infected.size.value, 1)
        self.assertEquals(recovered.size.value, 1)

    def test_can_update_population_on_based_on_dt(self):
        population = FixedPopulation()
        susceptable = population.create_compartment('susceptable', initial=1000)
        infected = population.create_compartment('infected', initial=1)
        model.set_population(population)
        dt = model.get_time_parameter()
        model.add_transition(susceptable, infected, Constant(2) * dt)
        model.step(4)
        self.assertEquals(susceptable.size.value, 992)
        self.assertEquals(infected.size.value, 9)

    def test_can_trace_several_timesteps(self):
        population = FixedPopulation()
        susceptable = population.create_compartment('susceptable', initial=1000)
        infected = population.create_compartment('infected', initial=1)
        model.set_population(population)
        dt = model.get_dt_parameter()
        model.add_transition(susceptable, infected, dt)
        self.assertEqual(
            model.trace(3, 1),
            [
                [0, 1000, 1],
                [1, 999 , 2],
                [2, 998,  3]
            ]
        )
