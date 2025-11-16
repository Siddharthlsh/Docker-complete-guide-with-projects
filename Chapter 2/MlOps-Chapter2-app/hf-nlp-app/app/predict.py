from transformers import pipeline
import os

# Load sentiment analysis pipeline
classifier = pipeline("sentiment-analysis",model = "./models/distilbert-base-uncased-finetuned-sst-2-english",tokenizer = "./models/distilbert-base-uncased-finetuned-sst-2-english")

# Load sample texts
input_file = "sample_text.txt"
with open(input_file, "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()] # this will remove leading-trailing whitespaces

# Run inference
results = classifier(lines)

# Print results
for line, result in zip(lines,results):
    print(f"line: {lines}")
    print(f"LABEL:{result['label']}, SCORE:{result['score']:.4f}")
    print("-" * 40)