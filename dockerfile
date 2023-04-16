FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y nmap
RUN pip install python-nmap

COPY . .

CMD [ "python", "./app.py" ]
