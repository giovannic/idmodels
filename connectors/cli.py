import argparse

def cli_executor(model):
    parser = argparse.ArgumentParser(
        description='Execute a stochastic infectious disease model'
    )

    parameters = model.get_parameters()

    for parameter in parameters:
        parser.add_argument(
            parameter.get_name(),
            type=float
        )

    args = parse_args()

    for parameter in parameters:
        parameter.set_value(getattr(args, parameter.get_name()))

    for row in model.trace():
        print('\t'.join(str(item) for out in row))
