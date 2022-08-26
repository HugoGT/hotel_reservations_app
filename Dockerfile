#Docker build fails


# FROM python:3.10
# ENV PYTHONUNBUFFERED 1

# COPY . usr/src/app
# WORKDIR /usr/src/app

# RUN apt-get update
# RUN apt-get install python3-dev default-libmysqlclient-dev build-essential -y
# RUN pip install -r requirements.txt
# RUN python manage.py makemigrations
# RUN python manage.py migrate
# RUN python manage.py collectstatic --noinput
