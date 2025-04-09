from flask import Flask
from flask_migrate import Migrate
from models import db
from routes import routes  # Import the Blueprint

def create_app():
    app = Flask(__name__)

    # Configurations
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)

    # Register blueprints
    app.register_blueprint(routes)

    return app

# Run the app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
