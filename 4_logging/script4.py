import logging.config
import click

def set_logger():
    logging.config.fileConfig('4_logging/logging.conf')
    logger = logging.getLogger()
    return logger

def div(a, b):
    y = a / b
    return y

def validate_arg(ctx, param, value):
    if value <= 0:
        raise click.BadParameter("Please input plus params")
    return value

@click.command()
@click.option('--arg1', callback=validate_arg, type=float, required=True, metavar='int_value', help="int argument")
@click.option('--arg2', callback=validate_arg, type=float, required=True, metavar='int_value', help="int argument")
def main(**kwargs):
    logger = set_logger()
    logger.info(f"params : {kwargs}")

    y = div(kwargs["arg1"], kwargs["arg2"])
    logger.info(f"result : {y}")

if __name__ == "__main__":
    main()