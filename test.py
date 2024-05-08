#dollars = 1
#cents = 10

import click

@click.command()
@click.option("--dollars", prompt = 'dollar')
@click.option("--cents", prompt = 'cents')

def function(dollars, cents):
    change = dollars*100 + cents
    return change
    print(function(10,10))

if __name__ == "__main__":
    function()