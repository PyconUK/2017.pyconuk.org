FROM alpine

RUN apk update && apk add nodejs-npm python3

# Required for lxml
RUN apk add build-base libxml2-dev libxslt-dev python3-dev

RUN npm install -g less

COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 8000

VOLUME ["/site"]
WORKDIR /site

CMD ["python3", "manage.py", "serve", "0.0.0.0:8000"]
