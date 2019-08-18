from core.models.disease import TemporalDiseaseModel
from core.models.population import FixedPopulationModel
from core.expressions import Constant
import unittest

class DiseaseModelTestCase(unittest.TestCase):

    def test_will_error_gracefully_when_not_parameterised(self):
        population = FixedPopulationModel()
        susceptable = population.create_compartment('susceptable', initial=1000)
        infected = population.create_compartment('infected', initial=1)
        model = TemporalDiseaseModel(population, 1)
        alpha = model.create_parameter('alpha')
        model.add_transition(susceptable, infected, alpha)
        with self.assertRaises(ValueError):
            model.trace(1, 1)
        alpha.set_value(1)
        model.trace(1, 1)

    def test_will_update_population_on_timestep(self):
        population = FixedPopulationModel()
        susceptable = population.create_compartment('susceptable', initial=1000)
        infected = population.create_compartment('infected', initial=1)
        model = TemporalDiseaseModel(population, 1)
        model.add_transition(susceptable, infected, Constant(1))
        model.trace(1, 1)
        self.assertEqual(susceptable.size.value, 999)
        self.assertEqual(infected.size.value, 2)

    def test_will_update_population_on_timestep_multiple_transitions(self):
        population = FixedPopulationModel()
        susceptable = population.create_compartment('susceptable', initial=1000)
        infected = population.create_compartment('infected', initial=1)
        recovered = population.create_compartment('recovered')
        model = TemporalDiseaseModel(population, 1)
        model.add_transition(susceptable, infected, Constant(1))
        model.add_transition(infected, recovered, Constant(1))
        model.trace(1, 1)
        self.assertEqual(susceptable.size.value, 999)
        self.assertEqual(infected.size.value, 1)
        self.assertEqual(recovered.size.value, 1)

    def test_can_update_population_on_based_on_dt(self):
        population = FixedPopulationModel()
        susceptable = population.create_compartment('susceptable', initial=1000)
        infected = population.create_compartment('infected', initial=1)
        model = TemporalDiseaseModel(population, 4)
        dt = model.dt_expression
        model.add_transition(susceptable, infected, Constant(2) * dt)
        model.trace(1, 1)
        self.assertEqual(susceptable.size.value, 992)
        self.assertEqual(infected.size.value, 9)

    def test_can_trace_several_timesteps(self):
        population = FixedPopulationModel()
        susceptable = population.create_compartment('susceptable', initial=1000)
        infected = population.create_compartment('infected', initial=1)
        model = TemporalDiseaseModel(population, 1)
        dt = model.dt_expression
        model.add_transition(susceptable, infected, dt)
        self.assertEqual(
            model.trace(3, 1),
            [
                ['t', 'susceptable', 'infected'],
                [0  , 1000         , 1         ],
                [1  , 999          , 2         ],
                [2  , 998          , 3         ]
            ]
        )
