"""Console script for oppenheimer."""

import click


@click.command()
def main():
    """Main entrypoint."""
    title = "Oppenheimer - Canvas Board"
    click.echo(title)
    click.echo("=" * len(title))
    click.echo("A tool for project management")

    from .view.qmlmainview import QmlMainView
    view = QmlMainView()
    view.show()


if __name__ == "__main__":
    main()  # pragma: no cover
