# Stage 1: Build dependencies
FROM python:3.11-alpine AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final runtime
FROM python:3.11-alpine
WORKDIR /app
COPY --from=builder /usr/local /usr/local
COPY app.py .
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
