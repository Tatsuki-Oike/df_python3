import logging.config
import click
import traceback

def set_logger():
    logging.config.fileConfig('5_try_except/logging.conf')
    logger = logging.getLogger()
    return logger

def div(a, b):
    y = a / b
    return y

def validate_arg(ctx, param, value):
    if value < 0:
        raise click.BadParameter("Please input plus params")
    return value

@click.command()
@click.option('--arg1', callback=validate_arg, type=float, required=True, metavar='float_value', help="float argument")
@click.option('--arg2', callback=validate_arg, type=float, required=True, metavar='float_value', help="float argument")
def main(**kwargs):
    logger = set_logger()
    logger.info(f"params : {kwargs}")
    
    try:
        y = div(kwargs["arg1"], kwargs["arg2"])
        logger.info(f"result : {y}")
    except:
        logger.error(traceback.format_exc())

if __name__ == "__main__":
    main()