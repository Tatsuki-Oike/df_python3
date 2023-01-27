import click

def validate_arg1(ctx, param, value):
    if value > 100:
        raise click.BadParameter("Invalid Params")
    return value

@click.command()

@click.argument('arg0', type=int, metavar='int_value')
@click.option('--arg1', callback=validate_arg1, type=int, required=True, metavar='int_value', help="int argument")
@click.option('--arg2', default="defalt_string", type=str, required=False, metavar='str_value', help="str argument")
@click.option('--arg3', default=False, is_flag=True, required=False, help="boolean argument")
@click.option('--arg5', default="a", type=click.Choice(["a", "b", "c"]),
    required=False, metavar='choice_value', help="choice argument")
def arg_function(arg0, arg1, **kwargs):
    print(arg0)
    print(arg1)
    print(kwargs)

def main():
    arg_function()

if __name__ == '__main__':
    main()