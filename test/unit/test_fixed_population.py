import unittest
from core.models.population import FixedPopulationModel

class FixedPopulationTestCase(unittest.TestCase):

    def test_cannot_create_invalid_compartments(self):
        population = FixedPopulationModel()
        population.initialise_expressions(1)
        with self.assertRaises(ValueError):
            population.create_compartment('susceptable', initial=-200)

    def test_will_transition_states(self):
        population = FixedPopulationModel()
        s = population.create_compartment('susceptable', initial=200)
        i = population.create_compartment('infected', initial=200)
        population.initialise_expressions(1)
        population.move(s, i, 10)
        self.assertEqual(s.size.value, 190)
        self.assertEqual(i.size.value, 210)

    def test_will_transition_correctly_at_zero(self):
        population = FixedPopulationModel()
        s = population.create_compartment('susceptable', initial=200)
        i = population.create_compartment('infected', initial=200)
        population.initialise_expressions(1)
        population.move(s, i, 300)
        self.assertEqual(s.size.value, 0)
        self.assertEqual(i.size.value, 400)

    def test_reports_the_correct_size(self):
        population = FixedPopulationModel()
        s = population.create_compartment('susceptable', initial=200)
        i = population.create_compartment('infected', initial=100)
        population.initialise_expressions(1)
        self.assertEqual(population.size.evaluate(), 300)

    #TODO: implement test for simulation size of 2
    def test_will_transition_correctly_for_multiple_simulations(self):
        pass
