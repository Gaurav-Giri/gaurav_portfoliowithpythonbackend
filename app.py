from flask import Flask
from flask_login import LoginManager
from models import db, User
from config.settings import Config
from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
# Initialize extensions
login_manager = LoginManager()
migrate = Migrate()
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(config_class)
    #db = SQLAlchemy() #  by chatgpt
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from blueprints.home.routes import home_bp
    from blueprints.projects.routes import projects_bp
    from blueprints.auth.routes import auth_bp
    from blueprints.contact.routes import contact_bp
    from blueprints.errors.handlers import errors_bp
    
    app.register_blueprint(home_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(errors_bp)
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)