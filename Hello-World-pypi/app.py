import click
"""
@click.group()
def cli():
    pass

@click.command()
@click.option('--count', default=1, help='number of times to echo')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo(f"Hello {name}!")


if __name__ == '__main__':
    cli()  """


@click.command()
def hello():
    click.echo('Hello World!')

if __name__ == '__main__':
    hello() 