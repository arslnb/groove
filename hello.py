###########################
####      GR00VE      #####
####       v0.1       #####
###########################


import click
import time

@click.command()
def hello():
	print("Hello")

@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        print('Hello %s!' % name)

if __name__ == '__main__':
	hello()