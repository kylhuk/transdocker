# Dockerfile

# Set the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Install necessary packages
RUN apt-get update && apt-get install -y git

# Copy the source code
COPY . /app

# Sync the github repo
RUN git clone https://github.com/kylhuk/transdocker.git

# Download the file
# RUN wget <url>

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start the python script
CMD ["python", "server.py"]

# Add labels
LABEL maintainer="librehub <librehub@proton.me>"
LABEL version="1.0"