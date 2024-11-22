import matplotlib

matplotlib.use("Agg")  # to suppress interactive plotting
import matplotlib.pyplot as plt
import numpy as np
from pysam import VariantFile
import seaborn as sns

window_size = 500

pos = [record.pos for record in VariantFile(snakemake.input[0])]
# setup windows
bins = np.arange(0, max(pos), window_size)

# use window midpoints as x coordinate
x = (bins[1:] + bins[:-1]) / 2

# compute variant density in each window
h, _ = np.histogram(pos, bins=bins)
y = h / window_size

# plot
fig, ax = plt.subplots(figsize=(12, 3))
sns.despine(ax=ax)  # , offset=10)
ax.plot(x, y)
ax.set_xlabel("Chromosome position (bp)")
ax.set_ylabel("Variant density (bp$^{-1}$)")
plt.savefig(snakemake.output[0])
