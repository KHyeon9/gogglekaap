from flask import Blueprint, flash, render_template, redirect, request, url_for, session

from werkzeug import security

from gogglekaap.forms.auth_form import LoginForm, RegisterForm
from gogglekaap.models.user import User as UserModel

NAME = "auth"
bp = Blueprint(NAME, __name__, url_prefix='/auth')

"""only for testing"""
from dataclasses import dataclass
USERS = []

@dataclass
class User:
    """
        class User:
            def __init__(self, user_id, user_name, password):
            self.user_id = user_id
            self.user_name = user_name
            self.password = password
    """
    user_id:str
    user_name:str
    password:str


USERS.append(User("mrk0607", "mrk", security.generate_password_hash("1234")))
USERS.append(User("admin", "admin", security.generate_password_hash("1234")))
USERS.append(User("tester", "tester", security.generate_password_hash("1234")))


@bp.route('/')
def index():
    return redirect(url_for(f"{NAME}.login"))

@bp.route('/login', methods=['GET', 'POST'])
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
        user = [user for user in USERS if user.user_id == user_id]

        if user:
            user = user[0]
            if not security.check_password_hash(user.password, password):
                flash("Password is not valid.")
            else:
                session["user_id"] = user_id
                return redirect(url_for(f"base.index"))
        else:
            flash("User ID is not exists.")

    else:
        # TODO: Error
        flash_form_errors(form)

    return render_template(f'{NAME}/login.html', form=form)

@bp.route('/logout')
def logout():
    session.pop("user_id", None)
    return redirect(url_for(f"{NAME}.login"))

@bp.route('/register', methods=['GET', 'POST'])
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
        user = [user for user in USERS if user.user_id == user_id]

        if user:
            flash("User ID is already exists.")
            return redirect(url_for(request.path))
        else:
            USERS.append(
                User(
                    user_id = user_id,
                    user_name = user_name,
                    password = security.generate_password_hash(password)
                )
            )

            session["user_id"] = user_id

            return redirect(url_for("base.index"))

    else:
        #TODO: Error
        flash_form_errors(form)

    return render_template(f'{NAME}/register.html', form=form)


def flash_form_errors(form):
    for _, errors in form.errors.items():
        for e in errors:
            flash(e)