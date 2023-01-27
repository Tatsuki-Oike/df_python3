import click

@click.group()
def subcmd_function():
    pass

@subcmd_function.command()
def subcmd1():
    print("subcmd1実行")

@click.command()
@click.option('--arg1', default="defalt_string", type=str,
    required=False, metavar='str_value', help="str argument")
def subcmd2(arg1):
    print(arg1)
    print("subcmd2実行")

subcmd_function.add_command(subcmd2)

if __name__ == '__main__':
    subcmd_function()