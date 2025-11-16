FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Download and cache the model during build
RUN python -c "from huggingface_hub import snapshot_download; snapshot_download('distilbert-base-uncased-finetuned-sst-2-english', local_dir='./models/distilbert-base-uncased-finetuned-sst-2-english')"

# Copy the rest of your code
COPY . .

# Run the app
CMD ["python", "predict.py"]
