#!/usr/bin/env python3
"""
Building a simple calculator module with addition, subtraction, multiplication, and division functions.
This command would be invoked as a CLI tool with click or imported as a module.
"""

import click

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

#build click group


@click.group()
def cli():
    """Simple Calculator CLI"""

@cli.command("add")
@click.argument('a', type=float)    
@click.argument('b', type=float)
def add_command(a, b):
    """Add two numbers."""
    result = add(a, b)
    click.echo(click.style(f"The sum of {a} and {b} is {result}", fg="green"))

@cli.command("subtract")
@click.argument('a', type=float)    
@click.argument('b', type=float)
def subtract_command(a, b):         
    """Subtract two numbers."""
    result = subtract(a, b)
    click.echo(click.style(f"The difference of {a} and {b} is {result}", fg="yellow"))

@cli.command("multiply")
@click.argument('a', type=float)    
@click.argument('b', type=float)
def multiply_command(a, b):         
    """Multiply two numbers."""
    result = multiply(a, b)
    click.echo(click.style(f"The product of {a} and {b} is {result}", fg="blue"))

@cli.command("divide")
@click.argument('a', type=float)    
@click.argument('b', type=float)
def divide_command(a, b):           
    """Divide two numbers."""
    try:
        result = divide(a, b)
        click.echo(click.style(f"The quotient of {a} and {b} is {result}", fg="red"))
    except ValueError as e:
        click.echo(click.style(str(e),fg="red"))


if __name__ == '__main__':
    cli()
