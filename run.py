logo = """

   ___                      
  / __|_ _ ___  _____ _____ 
 | (_ | '_/ _ \/ _ \ V / -_)
  \___|_| \___/\___/\_/\___|
                            

"""


import click
import time
import os
from colorama import init, Fore, Back, Style
init()


@click.command()
def hello():
	print(Fore.WHITE + logo)

if __name__ == '__main__':
	hello()