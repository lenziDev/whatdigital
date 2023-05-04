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

# copy react static files
COPY ./frontend/build /app/static

# run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]