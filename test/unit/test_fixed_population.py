import unittest
from core.population import FixedPopulation

class FixedPopulationTestCase(unittest.TestCase):

    def test_cannot_create_invalid_compartments(self):
        population = FixedPopulation()
        with self.assertRaises(ValueError):
            population.create_compartment('susceptable', initial=-200)

    def test_will_transition_states(self):
        population = FixedPopulation()
        s = population.create_compartment('susceptable', initial=200)
        i = population.create_compartment('infected', initial=200)
        population.move(s, i, 10)
        self.assertEqual(s.size.value, 190)
        self.assertEqual(i.size.value, 210)

    def test_will_transition_correctly_at_zero(self):
        population = FixedPopulation()
        s = population.create_compartment('susceptable', initial=200)
        i = population.create_compartment('infected', initial=200)
        population.move(s, i, 300)
        self.assertEqual(s.size.value, 0)
        self.assertEqual(i.size.value, 400)

    def test_reports_the_correct_size(self):
        population = FixedPopulation()
        s = population.create_compartment('susceptable', initial=200)
        i = population.create_compartment('infected', initial=100)
        self.assertEqual(population.size.value, 300)
