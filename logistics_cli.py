#!/usr/bin/env python
from logistics import distance_between, print_cities, find_coodinates, travel_time
import click


@click.group()


@click.command("cities")
def cities():
    click.echo(click.style("List of cities", fg="green"))
    for city in print_cities():
        click.echo(click.style("city", fg="blue"))


@click.command("distance")
@click.argument("city1")
@click.argument("city2")
def distance(city1,city2):
    click.echo(click.style("Distance between cities", fg="green"))
    click.echo(
        click.style(
            f"{distance_between(find_coodinates('city1'), find_coodinates(city2))} miles",
            fg="blue"
            )
            )


@click.command("travel")
@click.argument("city1")
@click.argument("city2")
@click.option("--speed", defaults=60, help="speed in mph")
def travel(city1, city2, speed):
    click.echo(click.style("Travel time  between cities", fg="green"))
    click.echo(
        click.style(
            f"{travel_time(city1, city2, speed)} hours",
            fg="blue"
            )
            )


#def total():
#    print(distance_miles(CITIES))

if __name__ == "__main__":
    cli()
