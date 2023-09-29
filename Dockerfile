FROM python:3.9

COPY . /app
WORKDIR /app

RUN python -m pip install -e .

CMD bash
