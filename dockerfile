FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy files
COPY . /app/

# Install Python deps with CPU-only PyTorch
RUN pip install --upgrade pip
RUN pip install --extra-index-url https://download.pytorch.org/whl/cpu -r requirements.txt

# Expose port
EXPOSE 10000

# Start the app
CMD ["python", "app.py"]
