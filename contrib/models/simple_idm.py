from connectors.cli import cli_executor
from core.models import IDModel,
from core.models.population import FixedPopulation
from core.models.inference import Binomial

model = IDModel()

# set up parameters
beta = model.create_parameter('beta')
sigma = model.create_parameter('sigma')

# set up population
population = FixedPopulation()
susceptable = population.create_compartment('susceptable', initial=1000)
infected = population.create_compartment('infected', initial=1)
recovered = population.create_compartment('recovered', initial=0)
model.set_population(population)

# time parameter
dt = model.get_time_parameter()

infection_inference = Binomial(
    susceptable.size_parameter(),
    beta * (infected.size_parameter() / population.size()) * dt
)

recovery_inference = Binomial(
    infected.size_parameter(),
    sigma * dt
)

# set up inference
model.add_transition(susceptable, infected, infection_inference)
model.add_transition(infected, recovered, recovery_inference)

if __name__ == '__main__':
    cli_executor(simple_idm)
