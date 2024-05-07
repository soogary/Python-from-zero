"""This bot calls a sub function mylib/bot.py which is used to fetch wikipedia content"""

import click
from mylib.bot import mylib_scrape


@click.command()
@click.option(
    "--name", prompt="Enter your wikipedia page to scrape", help="web page you want to scrape"
)

def scrape(name):
    result = mylib_scrape(name)
    click.echo(click.style(f"{result}:", bg="red", fg="blue"))


if __name__ == "__main__":
    scrape()

# print(scrape("Microsoft"))
