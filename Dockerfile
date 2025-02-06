FROM python:3.10.16-alpine

ENV PYTHONUNBUFFERED 1

# Create directory structure
RUN mkdir -p /app
WORKDIR /app

# Copy just the requirements file
COPY requirements.txt /app

# Install dependencies
RUN pip install --upgrade pip && pip install --default-timeout=100 -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose the port
EXPOSE 8000