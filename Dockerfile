FROM python:3.11-slim

# Setting working directory
WORKDIR /app

# Install netcat
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Installing dependencies
COPY src/requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copying project files
COPY src /app

# Copying entrypoint script and make it executable
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Expose gunicorn port
EXPOSE 8000

# Use the entrypoint script to run migrations, collectstatic, and start server
ENTRYPOINT ["/app/entrypoint.sh"]
