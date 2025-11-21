# Build stage
FROM python:3.11-slim as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies for building
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libpq-dev \
    pkg-config \
    libcairo2-dev \
    libpango1.0-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements*.txt ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements-prod.txt

# Runtime stage
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install runtime dependencies only
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN addgroup --system django && adduser --system --ingroup django django

# Create necessary directories and assign permissions
RUN mkdir -p /run/sockets /app/staticfiles /app/media && \
    chown -R django:django /app /run/sockets

# Copy dependencies from builder
COPY --from=builder /usr/local /usr/local

# Copy app code and ensure ownership
COPY --chown=django:django . /app

# Copy entrypoint
COPY --chown=django:django entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

USER django

EXPOSE 8000
ENTRYPOINT ["/app/entrypoint.sh"]
