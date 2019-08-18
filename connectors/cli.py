import argparse

def cli_executor(model):
    parser = argparse.ArgumentParser(
        description='Execute a stochastic infectious disease model'
    )

    parameters = model.parameters

    parser.add_argument(
        'steps',
        help='number of timesteps to trace',
        default=10,
        type=int
    )

    parser.add_argument(
        'simulations',
        help='number of timesteps to trace',
        default=3,
        type=int
    )

    for parameter in parameters:
        parser.add_argument(
            parameter.label,
            type=float
        )

    args = parser.parse_args()

    for parameter in parameters:
        parameter.set_value(getattr(args, parameter.label))

    for row in model.trace(args.steps, args.simulations):
        print('\t'.join(str(item) for item in row))
