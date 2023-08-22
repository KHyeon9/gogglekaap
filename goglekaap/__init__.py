from flask import Flask

def create_app():
    print("run create_app()")
    app = Flask(__name__)

    @app.route('/')
    def index():
        app.logger.info("RUN HELLOWORLD")
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

    """ Request Hook """
    from flask import g, current_app

    # @app.before_first_request   flask 2.3이후 버전 부터 제거됨
    # def before_first_request():
    #     app.logger.info('BEFORE FIRST REQUEST')

    @app.before_request
    def before_request():
        g.test = True
        app.logger.info("BEFORE REQUEST")


    @app.after_request
    def after_request(response):
        app.logger.info("AFTER REQUEST")
        app.logger.info(f"g.test: {g.test}")
        # app.logger.info(f"current_app.config: {current_app.config}")
        return response

    @app.teardown_request
    def teardown_request(exception):
        app.logger.info("TEARDOWN REQUEST")

    @app.teardown_appcontext
    def teardown_appcontext(exception):
        app.logger.info("TEARDOWN APPCONTEXT")

    return app