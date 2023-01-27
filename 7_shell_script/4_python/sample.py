import click

@click.command()
@click.option('--arg1', default=1, type=int)
@click.option('--arg2', default=False, is_flag=True)
def arg_function(**kwargs):
    print(kwargs)

def main():
    arg_function()

if __name__ == '__main__':
    main()