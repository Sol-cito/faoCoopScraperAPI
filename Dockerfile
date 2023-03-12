FROM python:3.9.6

MAINTAINER Dasol Kim

RUN pip install django
RUN pip install djangorestframework
RUN pip install django-filter

# 도커 이미지 내부에서 RUN, CMD 등의 명령어가 실행될 경로 설정
WORKDIR /usr/src/app

# 현재디렉터리(도커파일이 위치한)에 있는 파일들을 이미지 내부 WORKDIR 로 복사
COPY . .

# 컨테이너 run 하는 시점의 명령어
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

# 외부 노출 포트
EXPOSE 8000
