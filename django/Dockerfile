FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=app.base

WORKDIR /opt/find-anya-django

COPY requirements.txt /opt/find-anya-django/

RUN apt-get update
RUN apt-get install -y libpq-dev python3-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /opt/find-anya-django/

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
