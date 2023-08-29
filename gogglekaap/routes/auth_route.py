from flask import Blueprint, flash, render_template, redirect, request, url_for, session, g

from werkzeug import security

from gogglekaap.forms.auth_form import LoginForm, RegisterForm
from gogglekaap.models.user import User as UserModel

NAME = "auth"
bp = Blueprint(NAME, __name__, url_prefix='/auth')


@bp.before_app_request
def before_app_request():
    g.user = None
    user_id = session.get('user_id')

    if user_id:
        user = UserModel.find_one_by_user_id(user_id)

        if user:
            g.user = user
        else:
            session.pop(user_id, None)

@bp.route('/')
def index():
    return redirect(url_for(f"{NAME}.login"))

# 로그인
@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit(): # method가 POST이고 validator가 ok인 경우
        user_id = form.data.get("user_id")
        password = form.data.get("password")
        user = UserModel.find_one_by_user_id(user_id)

        if user:
            if not security.check_password_hash(user.password, password):
                flash("Password is not valid.")
            else:
                session['user_id'] = user.user_id
                return redirect(url_for(f"base.index"))
        else:
            flash("User ID is not exists.")

    else:
        flash_form_errors(form)

    return render_template(f'{NAME}/login.html', form=form)

# 로그아웃
@bp.route('/logout')
def logout():
    session.pop("user_id", None)
    return redirect(url_for(f"{NAME}.login"))

# 회원 가입
@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    user_id = form.user_id.data

    if form.validate_on_submit(): # method가 POST이고 validator가 ok인 경우
        user = UserModel.find_one_by_user_id(user_id)
        print(user)
        if user:
            flash("User ID is already exists.")
            return redirect(request.path)
        else:
            g.db.add(
                UserModel(
                    user_id=user_id,
                    user_name=form.user_name.data,
                    password=security.generate_password_hash(form.password.data)
                )
            )
            g.db.commit()
            session['user_id'] = user_id

            return redirect(url_for("base.index"))

    else:
        flash_form_errors(form)

    return render_template(f'{NAME}/register.html', form=form)


def flash_form_errors(form):
    for _, errors in form.errors.items():
        for e in errors:
            flash(e)