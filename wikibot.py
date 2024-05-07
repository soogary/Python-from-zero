# wikipedia.summary("Facebook", sentences=1)
# result = wikipedia.summary("Microsoft", sentences=1)
# print(result)

# ====

import wikipedia
import click


@click.command()
@click.option(
    "--name", prompt="your wikipedia page to scrape", help="web page you want to scrape"
)
@click.option("--length", prompt="Number of sentences", help="number of sentences")
def scrape(name="Microsoft", length=1):
    result = wikipedia.summary(name, sentences=length)
    click.echo(click.style(f"{result}:", bg="red", fg="blue"))


if __name__ == "__main__":
    scrape()

# print(scrape())
print(scrape("Microsoft"))
