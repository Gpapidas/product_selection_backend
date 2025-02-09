# Use official Python image
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1  # Prevents .pyc files
ENV PYTHONUNBUFFERED 1         # Ensures logs are visible

# Set working directory
WORKDIR /code

# Install system dependencies (vim, nano) and clean up cache
RUN apt-get update && apt-get install -y vim nano && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
COPY development.txt .

# Install dependencies based on the environment
ARG ENV_NAME
RUN if [ "$ENV_NAME" = "development" ]; then pip install -r development.txt; else pip install -r requirements.txt; fi

# Copy the rest of the application files
COPY . .

# Expose the port for the application
EXPOSE 80

# Default command: Run migrations, collect static, seed data, and start Gunicorn server
CMD sh -c 'python manage.py migrate && python manage.py collectstatic --noinput && python manage.py seeds && gunicorn product_selection_backend.wsgi:application --bind 0.0.0.0:80'
