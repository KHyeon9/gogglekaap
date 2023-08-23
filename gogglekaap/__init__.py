from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from gogglekaap.forms.auth_form import LoginForm, RegisterForm

csrf = CSRFProtect()

def create_app():
    print("run: create_app()")
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret'

    if app.config['DEBUG']:
        app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

    """ CSRF INIT """
    csrf.init_app(app)

    @app.route('/')
    def index():
        return render_template("index.html")

    @app.route('/auth/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()

        if form.validate_on_submit(): # method가 POST이고 validator가 ok인 경우
            # TODO
            # 1) 유저 조회
            # 2) 유저 존재 확인
            # 3) 유저 없으면 생성(회원 가입 페이지로)
            # 4) 로그인 유지(세션)
            user_id = form.data.get("user_id")
            password = form.data.get("password")

            return f"{user_id}, {password}"
        else:
            # TODO: Error
            pass

        return render_template('login.html', form=form)

    @app.route('/auth/logout')
    def logout():
        return 'logout'

    @app.route('/auth/register', methods=['GET', 'POST'])
    def register():
        form = RegisterForm()

        if form.validate_on_submit(): # method가 POST이고 validator가 ok인 경우
            # TODO
            # 1) 유저 조회
            # 2) 유저 존재 확인
            # 3) 유저 없으면 생성
            # 4) 로그인 유지(세션)
            user_id = form.data.get("user_id")
            user_name = form.data.get("user_name")
            password = form.data.get("password")
            repassword = form.data.get("repassword")

            return f"{user_id}, {user_name}, {password}, {repassword}"
        else:
            #TODO: Error
            pass

        return render_template('register.html', form=form)

    @app.errorhandler(404)
    def page_404(error):
        return render_template("404.html"), 404

    return app