# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy only requirements file first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Then copy the actual app
COPY app.py .

# Run the app
CMD ["python", "app.py"]
