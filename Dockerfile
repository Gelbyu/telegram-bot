FROM python:3.10
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN chmod 755 .

ENV PATH="/app"

COPY ./src .
COPY .env .

CMD ["python", "main.py"]