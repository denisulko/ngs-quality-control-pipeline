from pathlib import Path
import matplotlib.pyplot as plt

print("Script started")

file_path = Path("data/raw/sample.fastq")
print("File exists:", file_path.exists())

lengths = []

with open(file_path, "r") as f:
    lines = f.readlines()

print("Lines:", len(lines))

for i in range(1, len(lines), 4):
    seq = lines[i].strip()
    lengths.append(len(seq))

print("Lengths:", lengths)
print("Average:", sum(lengths)/len(lengths))

plt.hist(lengths, bins=10)
plt.xlabel("Read length")
plt.ylabel("Count")
plt.title("Read length distribution")

plt.savefig("results/read_lengths.png")

print("Image saved")