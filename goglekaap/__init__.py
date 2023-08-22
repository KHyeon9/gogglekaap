from flask import Flask

def create_app():
    print("run create_app()")
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Hello, World!"

    """ Routing Practice """
    from flask import jsonify, redirect, url_for
    from markupsafe import escape

    @app.route('/test/name/<name>')
    def name(name):
        return f"name is {name} and type is {escape(type(name))}"

    @app.route('/test/id/<int:id>')
    def id(id):
        return f"ID is {id}"

    @app.route("/test/path/<path:subpath>")
    def path(subpath):
        return f"SubPath is '{subpath}'"

    @app.route('/test/json')
    def json():
        return jsonify({"hello": "world"})

    @app.route('/test/redirect/<path:subpath>')
    def redirect_url(subpath):
        return redirect(subpath)

    @app.route('/test/urlfor/<path:subpath>')
    def urlfor(subpath):
        return redirect(url_for('path', subpath=subpath))

    return app