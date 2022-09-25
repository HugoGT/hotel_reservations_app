#Docker build fails
FROM python:3.10
ENV PYTHONUNBUFFERED 1

COPY . /code
WORKDIR /code

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential -y
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
CMD ["/bin/bash", "-c", "/code/scripts/runserver.sh"]
