FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    MALLOC_ARENA_MAX=2

RUN apt-get update && apt-get install -y --no-install-recommends \
        libgl1 \
        libglib2.0-0 \
        libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/api

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install torch==2.4.1 torchvision==0.19.1 \
        --extra-index-url https://download.pytorch.org/whl/cpu \
    && pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--workers", "1", "--threads", "4", "--timeout", "300", "--bind", "0.0.0.0:5000", "wsgi:app"]
