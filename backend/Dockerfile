FROM python:3.12-slim

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app/backend

EXPOSE 8000

CMD ["fastapi", "run", "backend/main.py", "--host", "0.0.0.0", "--port", "8000"]