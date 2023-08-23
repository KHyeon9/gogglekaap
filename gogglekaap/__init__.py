from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from gogglekaap.routes import base_route, auth_route

csrf = CSRFProtect()

def create_app():
    print("run: create_app()")
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret'

    if app.config['DEBUG']:
        app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

    """Routes INIT"""
    app.register_blueprint(base_route.bp)
    app.register_blueprint(auth_route.bp)

    """ CSRF INIT """
    csrf.init_app(app)



    @app.errorhandler(404)
    def page_404(error):
        return render_template("404.html"), 404

    return app