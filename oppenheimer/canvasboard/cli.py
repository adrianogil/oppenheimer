"""Console script for oppenheimer."""

def main():
    """Main entrypoint."""
    title = "Oppenheimer - Canvas Board"
    # click.echo(title)
    # click.echo("=" * len(title))
    # click.echo("A tool for project management")

    print("Oppenheimer - Canvas Board")
    from .view.qmlmainview import QmlMainView
    view = QmlMainView()
    view.show()


if __name__ == "__main__":
    main()  # pragma: no cover
