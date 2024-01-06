# Use a base image
FROM ubuntu:20.04

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY DataProccessing /app/DataProccessing
COPY cli_app.py /app
COPY requirements.txt /app
COPY settings.json /app
COPY setup /app
COPY cli_app /app

# Set environment variables to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Update the package repository
RUN apt-get update -y
RUN apt-get install ffmpeg libsm6 libxext6 -y

# Install GCC
RUN apt-get install gcc -y

# Install Python and Python virtual environment
RUN apt-get install -y python3 python3-pip python3-venv

# Make script executable
RUN chmod +x setup
RUN chmod +x cli_app

# Setup
RUN ./setup

# Define environment variable for Python to run in unbuffered mode for better logging
ENV PYTHONUNBUFFERED=1

# Run your Python application
CMD ["./cli_app"]