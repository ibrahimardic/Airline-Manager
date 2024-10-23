FROM ubuntu:latest

WORKDIR /app

RUN apt-get update && \
    apt-get install -y python3 python3-venv python3-pip curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN python3 -m venv /app/venv && \
    /bin/bash -c "source /app/venv/bin/activate && pip install --no-cache-dir -r requirements.txt"

EXPOSE 8000

CMD ["/app/venv/bin/python3", "manage.py", "runserver", "0.0.0.0:8000"]
