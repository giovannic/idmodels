from connectors.cli import cli_executor
from core.models.disease import TemporalDiseaseModel
from core.models.population import FixedPopulationModel
from core.expressions import Binomial

# set up our fixed population of S I R
population = FixedPopulationModel()
susceptable = population.create_compartment('susceptable', initial=1000)
infected = population.create_compartment('infected', initial=1)
recovered = population.create_compartment('recovered')

# set up our stochastic transformation of the infecious disease model:
# dS/dt = beta * S * I / N
# dI/dt = beta * S * I / N - sigma * I
# dR/dt = sigma * I
model = TemporalDiseaseModel(population, .1)
beta = model.create_parameter('beta')
sigma = model.create_parameter('sigma')
dt = model.dt_expression

infection_expression = Binomial(
    susceptable.size,
    beta * (infected.size / population.size) * dt
)

recovery_expression = Binomial(
    infected.size,
    sigma * dt
)

model.add_transition(susceptable, infected, infection_expression)
model.add_transition(infected, recovered, recovery_expression)

if __name__ == '__main__':
    cli_executor(model)
