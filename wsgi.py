from src.apps import app
from src.db import db

db.init_app(app)
with app.app_context():
    db.create_all()

application = app

if __name__ == "__main__":
    app.run(debug=True)
