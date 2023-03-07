FROM python:3.10
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirementx.txt
RUN chmod 755 .

COPY ./src .

CMD ["python", "main.py"]