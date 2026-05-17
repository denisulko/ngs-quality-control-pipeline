from pathlib import Path

file_path = Path("data/raw/sample.fastq")

with open(file_path, "r") as f:
    lines = f.readlines()

read_count = len(lines) // 4

print("Total reads:", read_count)
