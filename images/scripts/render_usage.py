import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager as fm

output_dir = Path(__file__).resolve().parent.parent / "efficiency"


with plt.xkcd():
    available_fonts = {font.name for font in fm.fontManager.ttflist}
    for font in ("Humor Sans", "Comic Neue", "xkcd", "xkcd Script", "Comic Sans MS", "StayPuft"):
        if font in available_fonts:
            plt.rcParams["font.family"] = [font]
            break
    else:
        warnings.warn("No sketch-style font found; using DejaVu Sans instead.")
        plt.rcParams["font.family"] = ["DejaVu Sans"]

    fig, ax = plt.subplots(figsize=(7, 3.5))

    # Step profile: time on x, resource usage on y
    # (plateau, jump, plateau, jump, plateau, drop)
    x = np.array([0.0, 2.2, 2.2, 3.0, 3.0, 5.5, 5.5, 5.9, 5.9, 6.2])
    y = np.array([0.5, 0.5, 3.5, 3.5, 1.8, 1.8, 3.1, 3.1, 0.6, 0.6])
    ax.plot(x, y, color="tab:blue", lw=2.5)

    # Maximum line
    maximum = 3.7
    ax.axhline(maximum, color="red", ls="--", lw=2.5)
    ax.text(0.4, 3.85, "MAX / roof", color="red", fontsize=12, fontweight="bold")

    # Step labels
    ax.text(0.9, 0.7, "step 1", fontsize=11)
    ax.text(2.6, 3.05, "step 2", fontsize=11, ha="center")
    ax.text(3.6, 1.95, "step 3", fontsize=11)
    ax.text(5.0, 3.25, "step 4", fontsize=11)
    ax.text(6.25, 0.8, "step 5", fontsize=11)

    # Axes
    ax.set_xlim(0, 7.5)
    ax.set_ylim(0, 4.6)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("time ->", fontsize=13)
    ax.set_ylabel("resources (CPU and RAM)", fontsize=13)

    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)

    fig.savefig(output_dir / "pipeline_xkcd.png", dpi=150, bbox_inches="tight")

    ax.fill_between(x, y, maximum, color="red", alpha=0.25, zorder=0)
    fig.savefig(output_dir / "pipeline_xkcd_waste.png", dpi=150, bbox_inches="tight")
