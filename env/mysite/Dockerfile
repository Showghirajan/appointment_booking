FROM python:3.10-slim

WORKDIR /medico

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    pkg-config \
    default-libmysqlclient-dev \
    gcc \
    libmariadb-dev \
    tzdata && \
    rm -rf /var/lib/apt/lists/*

# Copy the Django project files
COPY . /medico/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port and run the server
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


