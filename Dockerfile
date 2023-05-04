# base image
FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /app
RUN python manage.py collectstatic --noinput
EXPOSE 80

# run server

CMD ["uwsgi", "--http=0.0.0.0:80", "--module=whatdigital.wsgi"]