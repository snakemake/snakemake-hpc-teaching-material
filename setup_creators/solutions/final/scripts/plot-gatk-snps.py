import gzip

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

positions = {}
with gzip.open(snakemake.input[0], "rt") as vcf:
    for line in vcf:
        if line.startswith("#"):
            continue
        contig, position = line.split("\t", 2)[:2]
        positions.setdefault(contig, []).append(int(position))

if positions:
    contigs = list(positions)
    fig, ax = plt.subplots(figsize=(12, max(3, len(contigs) * 0.45)))
    for index, contig in enumerate(contigs):
        ax.scatter(positions[contig], [index] * len(positions[contig]), s=8)
    ax.set_yticks(range(len(contigs)), labels=contigs)
    ax.set_xlabel("Position within contig (bp)")
    ax.set_ylabel("Contig")
    ax.set_title("SNP positions identified by GATK")
else:
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.text(0.5, 0.5, "No SNPs were called", ha="center", va="center")
    ax.set_axis_off()

fig.tight_layout()
fig.savefig(snakemake.output[0])
