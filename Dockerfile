# Dockerfile for Hugging Face Spaces
# This Dockerfile is optimized for running Stable Diffusion WebUI on Hugging Face Spaces

FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    wget \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements_versions.txt /app/
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements_versions.txt

# Copy the application
COPY . /app/

# Set environment variables for Spaces
# Note: COMMANDLINE_ARGS can be overridden; if not set, app.py uses sensible defaults
ENV GRADIO_ANALYTICS_ENABLED="False"
ENV GRADIO_SERVER_NAME="0.0.0.0"

# Expose the port
EXPOSE 7860

# Run the application
CMD ["python", "app.py"]
