FROM python:3.13-slim

WORKDIR /getID

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py app.py
COPY ips.txt ips.txt

EXPOSE 5000

CMD [ "python", "app.py"]



