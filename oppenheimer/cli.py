"""Console script for oppenheimer."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("oppenheimer")
    click.echo("=" * len("oppenheimer"))
    click.echo("A tool for project management")


if __name__ == "__main__":
    main()  # pragma: no cover
