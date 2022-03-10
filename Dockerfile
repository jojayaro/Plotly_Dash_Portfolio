FROM ubuntu:latest
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3-pip -y
 
RUN mkdir wd
WORKDIR wd
COPY app/requirements.txt .
RUN pip3 install -r requirements.txt

COPY app/ ./

EXPOSE 8501

CMD ["gunicorn", "-b 0.0.0.0:8501", "-w 5", "--worker-class=gevent", "--timeout=90", "--threads=1", "--max-requests=100", "--max-requests-jitter=10", "index:server"]
