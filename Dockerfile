FROM ubuntu:latest
RUN apt-get update
RUN apt-get upgrade
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
 
RUN mkdir wd
WORKDIR wd
COPY app/requirements.txt .
RUN pip3 install -r requirements.txt

COPY app/ ./

EXPOSE 8501

CMD [ "gunicorn", "--workers=5", "--threads=1", "-b 0.0.0.0:8501", "app:server"]
