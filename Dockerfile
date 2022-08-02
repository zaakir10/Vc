FROM nikolaik/python-nodejs:python3.9-nodejs16

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y

RUN mkdir /abhi/
WORKDIR /abhi/
COPY . /abhi/

RUN pip3 install --upgrade pip
RUN pip3 install -U -r requirements.txt

CMD python3 -m Client
