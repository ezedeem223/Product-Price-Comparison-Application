# Dockerfile - Product Price Comparison App
# Customized by Ezedeen (ezedeem223) - IBM Microservices Final Project 2026
FROM python:3.8-slim-buster


WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "-p", "5001"]

LABEL maintainer="Ezedeen <ezedeem223@github.com>"
LABEL version="1.0-ezedeen"
LABEL description="Product Price Comparison - IBM Microservices Final Project"
