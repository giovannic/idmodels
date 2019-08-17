# Infectious disease models

TODO: make friendly

This codebase is for creating and simulating infectious disease models.

## Running models from the command line

TODO: make friendly

### Environment

* Python3 + virtualenv
* Docker

Contributed models are stored in contrib/models

executing `python -m contrib.models.[your disease model] -h` will give you the
help text for your model.

## Building your own models

You can add new models to contrib/models. Here is an example of how to build
your model.

```python
# Import models
from core.models.population import FixedPopulationModel
from core.models.disease import TemporalDiseaseModel

# Import expressions
from core.expressions import Constant

# Import a cli for your model
from connectors.cli

# define your population
population = FixedPopulationModel()
susceptable = population.create_compartment('susceptable', initial=1000)
infected = population.create_compartment('infected', initial=1)

# define your disease model
# here we use a simple temporal model with a time step of 0.5
disease_model = TemporalDiseaseModel(population, .5)

# create an expression for the transmission of disease
dt = disease_model.dt_expression
disease_model.add(dt * Constant(3))

# create a basic cli for your model
if __name__ == '__main__':
    cli_executor(disease_model)
```

## Developing the framework

TODO: make friendly

* run tests
* 

## Extensions

 * Disease intervention models
 * Spatio-temporal models
 * Compute backend for expressions (tensorflow, pytorch, theano, edward...)
 * Graphical output

## Project growth

 * Wiki page
 * Build and host documentation
