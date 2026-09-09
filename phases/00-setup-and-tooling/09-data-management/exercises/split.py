from datasets import load_dataset

dataset = load_dataset("stanfordnlp/imdb", split="train")

# 80% train, 20% temporary
split = dataset.train_test_split(test_size=0.2, seed=42)

train_ds = split["train"]

# Split the 20% into 10% validation and 10% test
val_test = split["test"].train_test_split(test_size=0.5, seed=42)

val_ds = val_test["train"]
test_ds = val_test["test"]

print(f"Train: {len(train_ds)}, Val: {len(val_ds)}, Test: {len(test_ds)}")
