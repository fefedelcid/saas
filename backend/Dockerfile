FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONBUFFERED=1

RUN apt-get update \
# dependencies for building Python packages
&& apt-get install -y build-essential \
# psycopg2 dependencies
&& apt-get install -y libpq-dev gcc \
# Translations dependencies
&& apt-get install -y gettext \
# cleaning up unused files
&& apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
&& rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY . /app/backend

EXPOSE 8000

CMD ["fastapi", "run", "backend/main.py", "--host", "0.0.0.0", "--port", "8000"]