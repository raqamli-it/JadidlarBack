# Base image
FROM python:3.10

# Working directory
WORKDIR /Jadidlar

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /Jadidlar/
RUN pip install --upgrade pip==23.0.1
RUN pip3 install -r requirements.txt

# Create and set permissions for staticfiles folder
RUN mkdir -p /Jadidlar/staticfiles
RUN chmod 755 /Jadidlar/staticfiles

# Copy project files
COPY . /Jadidlar/

# Collect static files
RUN python manage.py collectstatic --noinput

# Django settings
ENV DJANGO_SETTINGS_MODULE=config.settings

# Expose port
EXPOSE 5300

# Run migrations and start Daphne server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
