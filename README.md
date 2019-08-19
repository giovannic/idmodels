# Infectious disease models

This codebase is for creating and simulating infectious disease models.

## Running models from the command line

Firstly, let's make sure you have an environment to execute the model

### Environment

Please make sure you have Python 3 installed. The dependencies are listed in
requirements.txt. you can install them with:

`pip install -r requirements.txt`

### Running pre-made models

Contributed models are stored in contrib/models

executing `python -m contrib.models.[your disease model] -h` will give you the
help text for your model.

You can execute a model with the following code:

```
python -m contrib.models.simple_idm 100 1 10 1
```

To run a simple model and print out a trace

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
disease_model.add_transition(dt * Constant(3))

# create a basic cli for your model
if __name__ == '__main__':
    cli_executor(disease_model)
```

## Developing the framework

The framework is split into `core`, `test` `contrib`, `connectors` and `test`

**core**

These are the reusable parts of the framework for use by epidemiology
researchers. It consists of high-level classes to abstract out the complexities
of probabilistic programming. It has been split into:

 * core.expressions: These are abstractions for the mathematical expressions
that make up infectious disease models. It will handle the actual computation
in model simulations
 * core.models.population: These are classes to represent population models
 * core.models.disease: These are classes to represent disease transmission
models in a population

**connectors**

These are interfaces for the modelling code. Currently only the CLI connector
is implemented.

**test**

You can run tests using `python -m unittest discover`. Please write e2e tests 
before implementing new features and unittests while you're developing.

**contrib**

These are where contributed models are stored

## Extensions

 * Disease intervention models
 * Different population models
 * Compute backend for expressions (tensorflow, pytorch, theano, edward...)
 * Graphical output

## Project growth

 * Wiki page
 * Build and host documentation
 * Set coding conventions (e.g. variable naming to distinguish between model expressions and python variables)
