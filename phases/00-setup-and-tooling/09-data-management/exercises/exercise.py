from datasets import load_dataset
import time
import os

# Load the glue dataset with the mrpc config and inspect the first 5 examples
dataset = load_dataset("nyu-mll/glue", "mrpc")

print(dataset)
print(dataset["train"][:5])

# Stream the c4 dataset and count how many examples you can process in 10 seconds
dataset = load_dataset("allenai/c4", "en", split="train", streaming=True)

start = time.time()
count = 0

for example in dataset:
    count += 1

    if time.time() - start >= 10:
        break

print(f"Processed {count} examples in 10 seconds")


# Convert a dataset to Parquet and compare the file size to CSV
dataset = load_dataset("nyu-mll/glue", "mrpc", split="train")

dataset.to_parquet("mrpc.parquet")

dataset.to_csv("mrpc.csv")

parquet_size = os.path.getsize("mrpc.parquet")
csv_size = os.path.getsize("mrpc.csv")

print(f"Parquet: {parquet_size:,} bytes")
print(f"CSV:     {csv_size:,} bytes")

print(f"Parquet / CSV = {parquet_size / csv_size:.2%}")

# Create a 70/15/15 train/val/test split with a fixed seed and verify the sizes
dataset = load_dataset("nyu-mll/glue", "mrpc", split="train")

split = dataset.train_test_split(test_size=0.30, seed=42)
train_ds = split["train"]
val_test = split["test"].train_test_split(test_size=0.50, seed=42)
val_ds = val_test["train"]
test_ds = val_test["test"]

print(f"Total: {len(dataset)}")
print(f"Train: {len(train_ds)}")
print(f"Val:   {len(val_ds)}")
print(f"Test:  {len(test_ds)}")
