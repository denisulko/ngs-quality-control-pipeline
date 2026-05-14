from pathlib import Path
import pandas as pd

file_path = Path("data/raw/sample.fastq")

lengths = []

with open(file_path, "r") as f:
    lines = f.readlines()

for i in range(1, len(lines), 4):
    seq = lines[i].strip()
    if len(seq) > 0:
        lengths.append(len(seq))

df = pd.DataFrame({
    "read_length": lengths
})

summary = pd.DataFrame({
    "metric": ["read_count", "avg_length", "min_length", "max_length"],
    "value": [
        len(lengths),
        df["read_length"].mean(),
        df["read_length"].min(),
        df["read_length"].max()
    ]
})

summary.to_csv("results/qc_summary.csv", index=False)

print(summary)