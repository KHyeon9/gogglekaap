from flask import Flask, render_template, g
from flask_wtf.csrf import CSRFProtect

from flask_migrate import Migrate

from gogglekaap.routes import base_route, auth_route
from gogglekaap.exts import db
from gogglekaap.apis import blueprint as api

from .configs import DevelopmentConfig, ProductionConfig

csrf = CSRFProtect()
migrate = Migrate()

def create_app(config=None):
    print("run: create_app()")
    app = Flask(__name__)

    """Flask Configs"""
    if not config:
        if app.config['DEBUG']:
            config = DevelopmentConfig
        else:
            config = ProductionConfig

    print('run with: ', config)
    app.config.from_object(config)

    """ CSRF INIT """
    csrf.init_app(app)

    """DB INIT"""
    db.init_app(app)

    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    """Routes INIT"""
    app.register_blueprint(base_route.bp)
    app.register_blueprint(auth_route.bp)

    """Restx INIT"""
    app.register_blueprint(api)

    """REQUEST HOOK"""
    @app.before_request
    def before_request():
        g.db = db.session

    @app.teardown_request
    def teardown_request(exception):
        if hasattr(g, 'db'):
            g.db.close()

    @app.errorhandler(404)
    def page_404(error):
        return render_template("404.html"), 404

    return app