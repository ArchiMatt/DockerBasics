FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

WORKDIR /app
COPY . /app

RUN python3 -m venv venv

RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1
ENV PATH="/app/venv/bin:$PATH"

CMD ["python", "app.py"]