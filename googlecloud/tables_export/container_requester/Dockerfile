# docker build -t gcr.io/cool-ml-demos/requester:latest

FROM google/cloud-sdk:latest

RUN apt install -y python3-venv python3-pip
RUN python3.7 -m pip install google-cloud-logging
RUN python3.7 -m pip install requests

RUN mkdir app
WORKDIR /app
COPY local_request.py /app

ENTRYPOINT ["python3.7", "local_request.py"]