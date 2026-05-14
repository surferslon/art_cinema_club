FROM python:3.13-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

WORKDIR /app
COPY pyproject.toml ./
RUN /root/.local/bin/uv sync
COPY . .
ENV DJANGO_DEBUG=False
RUN /root/.local/bin/uv run python manage.py collectstatic --noinput

EXPOSE 8080

CMD ["/root/.local/bin/uv", "run", "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8080"]
