FROM python:3.12

RUN apt-get update && apt-get install -y bash

WORKDIR /app

ENV PYTHONPATH=/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY run_migrations.sh /app/run_migrations.sh
RUN chmod +x /app/run_migrations.sh

CMD ["sh", "-c", "./run_migrations.sh && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"]
