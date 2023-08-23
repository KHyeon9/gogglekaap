from flask import Blueprint, render_template

from gogglekaap.forms.auth_form import LoginForm, RegisterForm

NAME = "auth"
bp = Blueprint(NAME, __name__, url_prefix='/auth')

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

        return f"{user_id}, {password}"
    else:
        # TODO: Error
        pass

    return render_template(f'{NAME}/login.html', form=form)

@bp.route('/logout')
def logout():
    return 'logout'

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

        return f"{user_id}, {user_name}, {password}, {repassword}"
    else:
        #TODO: Error
        pass

    return render_template(f'{NAME}/register.html', form=form)