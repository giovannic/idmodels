from connectors.cli import cli_executor
from core.models import IDModel,
from core.models.population import FixedPopulation
from core.models.expressions import binomial


# set up population
population = FixedPopulation()
susceptable = population.create_compartment('susceptable', initial=1000)
infected = population.create_compartment('infected', initial=1)
recovered = population.create_compartment('recovered')

# set up disease model
model = IDModel(population, .1)
beta = model.create_parameter('beta')
sigma = model.create_parameter('sigma')
dt = model.dt_parameter

infection_expression = Binomial(
    susceptable.size_parameter(),
    beta * (infected.size / population.size) * dt
)

recovery_expression = Binomial(
    infected.size,
    sigma * dt
)

model.add_transition(susceptable, infected, infection_expression)
model.add_transition(infected, recovered, recovery_expression)

if __name__ == '__main__':
    cli_executor(simple_idm)
