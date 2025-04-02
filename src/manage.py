from flask.cli import FlaskGroup

from src.apps import app

cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()
