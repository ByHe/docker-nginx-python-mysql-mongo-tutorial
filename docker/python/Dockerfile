FROM python:3

WORKDIR /usr/src/server

COPY www/server/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY www/server/ ./

CMD ["python", "server.py"]