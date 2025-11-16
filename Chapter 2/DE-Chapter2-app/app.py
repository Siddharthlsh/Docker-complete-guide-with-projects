import pandas as pd

# Download dataset from URL
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
df = pd.read_csv(url)

# Clean up column names
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Drop missing values
df = df.dropna()

# Save cleaned data
df.to_csv("processed.csv", index=False)
print("✅ Data processed and saved to processed.csv")

print("✅ Experimenting with Layer Catching")