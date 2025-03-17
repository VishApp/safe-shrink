FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]
