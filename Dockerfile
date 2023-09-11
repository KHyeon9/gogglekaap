FROM python:3.11

# root 권한
# 유저 추가, 패스워드를 입력하지 않아도 되게끔 설정, 그리고 홈 디렉터리도 자동으로 생성
RUN adduser -disabled-password python

# 위에서 생성한 python 유저로 전환 (root -> python)
USER python

# 의존성 패키지 복사
COPY ./requirements.txt /tmp/requirements.txt

# 의존성 패키지 설치
RUN pip install --user -r /tmp/requirements.txt
RUN pip install --user gunicorn==20.1.0

# 프로젝트 복사
COPY --chown=python:python ./ /var/www/gogglekaap

# 복사한 프로젝트로 이동
WORKDIR /var/www/gogglekaap

# 설치한 패키지 명령어를 사용하기 위해 환경변수를 등록
ENV PATH="/home/python/.local/bin:${PATH}"

# 8080포트를 노출
EXPOSE 8080

# 유니콘 실행
CMD gunicorn --bind :8080 --workers 2 --threads 8 'gogglekaap:create_app()'