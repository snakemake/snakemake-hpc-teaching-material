import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager as fm

output_dir = Path(__file__).resolve().parent.parent / "efficiency"

# ---------------------------------------------------------------------------
# Sketch style.  Picked once and applied globally: inside a `with plt.xkcd():`
# block the rcParams (including font.family) are restored on exit, so the old
# version actually plotted in the default style.
# ---------------------------------------------------------------------------
available_fonts = {font.name for font in fm.fontManager.ttflist}
for font in ("Humor Sans", "Comic Neue", "xkcd", "xkcd Script",
             "Comic Sans MS", "StayPuft"):
    if font in available_fonts:
        SKETCH_FONT = font
        break
else:
    warnings.warn("No sketch-style font found; using DejaVu Sans instead.")
    SKETCH_FONT = "DejaVu Sans"

plt.xkcd(scale=1.0, length=100, randomness=2.0)   # persistent, not a context
plt.rcParams["font.family"] = [SKETCH_FONT]


# ---------------------------------------------------------------------------
# 1) Original single-panel figure
# ---------------------------------------------------------------------------
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


# ---------------------------------------------------------------------------
# 2) NEW: per-node step profiles, Node 1 ... Node N
# ---------------------------------------------------------------------------
N_CPUS = 384          # real core count of the node
x_max = N_CPUS        # ceiling -> red dashed roof line
T_END = 35.0          # 5 + 10 + 5 + 5 + 10 min


def step_profile(stages=None, t0=0.0):
    """Staircase polyline: core count (x) held constant, time (y) advancing.

    stages: list of (cores, duration_minutes).  Each entry is one plateau;
    between two plateaus the core count jumps instantaneously (horizontal
    segment at constant time), exactly the plateau/jump style of part 1.
    """
    if stages is None:
        stages = [
            (1,     5.0),    # low usage
            (N_CPUS, 10.0),  # full usage
            (32,    5.0),
            (192,   5.0),
            (8,    10.0),    # rest of the run
        ]
    xs, ys, t = [], [], t0
    for cores, duration in stages:
        xs += [cores, cores]          # vertical plateau at constant core count
        ys += [t, t + duration]
        t += duration                 # next stage starts with a horizontal jump
    return np.array(xs), np.array(ys)


fig2 = plt.figure(figsize=(13, 5.6))
gs = fig2.add_gridspec(1, 5, width_ratios=[1, 1, 1, 0.55, 1])
axes = [fig2.add_subplot(gs[0, 0]),
        fig2.add_subplot(gs[0, 1]),
        fig2.add_subplot(gs[0, 2]),
        fig2.add_subplot(gs[0, 4])]
fig2.subplots_adjust(left=0.06, right=0.98, bottom=0.17, top=0.96, wspace=0.55)

for i, ax in enumerate(axes):
    rng = np.random.default_rng(i)                    # per-node variation
    stages = [
        (1,                                    5.0),
        (N_CPUS,                              10.0 + rng.uniform(-0.8, 0.8)),
        (32  + rng.uniform(-3, 3),             5.0 + rng.uniform(-0.4, 0.4)),
        (192 + rng.uniform(-8, 8),             5.0 + rng.uniform(-0.4, 0.4)),
        (8   + rng.uniform(-1, 1),            10.0),
    ]
    x, y = step_profile(stages)

    line, = ax.plot(x, y, color="tab:blue", lw=2.0)
    # Keep the vertical plateaus vertical despite the xkcd wiggle
    line.set_sketch_params(scale=1.0, length=100.0, randomness=1.2)

    # Roof marker
    ax.axvline(x_max, color="red", ls="--", lw=1.8)
    ax.text(x_max + 6, 2.0, "roof", color="red",
            fontsize=11, ha="left", va="center")

    # Axes: no numbering on the time axis
    ax.set_xlim(0, 430)
    ax.set_ylim(0, T_END + 1.5)
    ax.set_xticks([0, 192, 384])
    ax.set_yticks([])
    ax.tick_params(labelsize=10)
    ax.set_xlabel("number of cores", fontsize=11)
    ax.set_ylabel("time \u2192", fontsize=11)

    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)

    caption = f"Node {i + 1}" if i < 3 else "Node N"
    ax.text(0.5, -0.34, caption, transform=ax.transAxes,
            ha="center", va="top", fontsize=17)

# Ellipsis between panel 3 and panel N
ax_dots = fig2.add_subplot(gs[0, 3])
ax_dots.axis("off")
ax_dots.text(0.5, 0.5, "...", ha="center", va="center", fontsize=28)

fig2.savefig(output_dir / "pipeline_xkcd_node.png", dpi=150,
             bbox_inches="tight")