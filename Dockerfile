# FROM registry.avantiplc.net:8443/avanti/python36:dev 
FROM python:3.8

RUN mkdir /opt/project
WORKDIR /opt/project
# COPY . .
COPY requirements.txt /opt/project
RUN apt update && apt install -y ffmpeg
RUN python3 -m pip install -r requirements.txt
CMD ["python", "web/manage.py", "runserver", "3000"]

