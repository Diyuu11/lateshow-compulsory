from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from models import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)  # <-- this line enables flask db commands
@app.route('/')
def index():
    return {"message": "Server is running"}

# Add your route imports and register them here
if __name__ == '__main__':
    app.run(port=5555, debug=True)
