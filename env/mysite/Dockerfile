FROM python:3.10-slim

WORKDIR /medico

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    iputils-ping \
    mariadb-client \  
    netcat-openbsd \
    pkg-config \
    default-libmysqlclient-dev \
    gcc \
    libmariadb-dev \
    tzdata && \
    rm -rf /var/lib/apt/lists/*

# Copy the Django project files
COPY . /medico/

# Install Python dependencies, including gunicorn
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Command to run gunicorn (production server)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mysite.wsgi:application"]