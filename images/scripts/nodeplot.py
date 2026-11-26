"""
Alternative figure: a timeline of a 5-node cluster, in the style of the
first pipeline/cluster figure.

Each time row shows all 5 nodes of the cluster. Each node can hold
 - 16 small boxes, 8 slightly bigger boxes, 2 mid-size boxes, or
   1 big box of a given workflow.
The primary workflow A is brick red (as before); the remaining capacity is
partially filled with works of users B..E in matching colours, one colour
per user. The y axis represents time (not linear).

Grey = compute nodes ("nodes") of the cluster.

The legend is placed below the plot so it never overlaps.

Requires: matplotlib >= 3.6   (run:  python cluster_utilization.py)
"""

"""
Reproduction of a pipeline/cluster diagram.

Grey rounded rectangles are compute nodes ("nodes") of a cluster, brick-red
rounded rectangles are computation steps of a pipeline, their size hinting at
the resource demand. The y axis represents time (not linear, only roughly
"later is higher").

Requires: matplotlib   (run:  python pipeline_figure.py)
"""

from pathlib import Path

output_dir = Path(__file__).resolve().parent.parent / "efficiency"

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Patch


# First figure: Distribution by a workflow

# ---------------------------------------------------------------- settings
NODE_COLOR = "grey"
STEP_COLOR = "firebrick"
NODE_ALPHA = 0.55          # transparency of the node fill
STEP_ALPHA = 0.80          # transparency of the step fill
NODE_W  = 2.0              # node width  in slot units (2 slots side by side)
NODE_H  = 2.0              # node height in slot units
COL_GAP = 0.6              # gap between nodes in a row
ROW_GAP = 1.4              # vertical gap between time rows
INNER   = 0.08             # margin of a step inside its slot area

# ----------------------------------------------------------- row contents
# Each row (time step) is a list of nodes. A node is a list of rectangles,
# each given as (x, y, w, h) in slot units inside the node (0..2, 0..2).
# The node itself acts as a 2x2 grid of compute slots; steps may fill one
# slot, a column of slots, the whole node, or be small sub-slot steps.

def slot(x, y):                       # one single slot
    return [(x + INNER, y + INNER, 1 - 2 * INNER, 1 - 2 * INNER)]

def slot_col(x):                      # one column of two slots (full height)
    return [(x + INNER, INNER, 1 - 2 * INNER, NODE_H - 2 * INNER)]

def whole_node():                     # one big step using both slot columns
    return [(INNER, INNER, NODE_W - 2 * INNER, NODE_H - 2 * INNER)]

def small_steps():                    # five small steps (grid, like top row)
    s, d = 0.05, 0.42
    return [
        (d, 1.55, 0.40, 0.40), (d + 0.50, 1.55, 0.40, 0.40),
        (d, 1.05, 0.40, 0.40), (d + 0.50, 1.05, 0.40, 0.40),
        (d, 0.55, 0.40, 0.40),
    ]

def wide_small_steps():               # five small wide steps (bottom row)
    d = 0.08
    return [
        (d, 1.60, 0.82, 0.34), (d + 0.94, 1.60, 0.82, 0.34),
        (d, 1.10, 0.82, 0.34), (d + 0.94, 1.10, 0.82, 0.34),
        (d, 0.60, 0.82, 0.34),
    ]

ROWS = [
    # time step 0 (top): one node, five small steps
    [small_steps()],
    # time step 1: full node, full node, half-full node
    [slot_col(0) + slot_col(1), slot_col(0) + slot_col(1), slot_col(0)],
    # time step 2: five nodes, each running one big step
    [whole_node() for _ in range(5)],
    # time step 3 (bottom): one node, five small wide steps
    [wide_small_steps()],
]

# ------------------------------------------------------------------ draw
fig, ax = plt.subplots(figsize=(11, 7.5))

node_step_x = NODE_W + COL_GAP

def rounded(x, y, w, h, color, alpha, rs=0.12, lw=1.2):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={rs}",
        facecolor=color, edgecolor=color, alpha=alpha, linewidth=lw))

for r, row in enumerate(ROWS):
    y0 = r * (NODE_H + ROW_GAP)
    for n, node in enumerate(row):
        x0 = n * node_step_x
        # node outline/fill (grey)
        rounded(x0, y0, NODE_W, NODE_H, NODE_COLOR, NODE_ALPHA, rs=0.18, lw=1.5)
        # steps (brick red)
        for (sx, sy, sw, sh) in node:
            rounded(x0 + sx, y0 + sy, sw, sh, STEP_COLOR, STEP_ALPHA, rs=0.08)

# ------------------------------------------------------- axes and legend
ax.set_xlim(-0.8, 5 * node_step_x)
ax.set_ylim(-0.6, 4 * (NODE_H + ROW_GAP))

ax.set_ylabel("Time (not linear)", fontsize=13)
ax.set_xticks([])
ax.set_yticks([])
for spine in ("top", "right", "bottom"):
    ax.spines[spine].set_visible(False)

# arrow pointing up along the time axis
ax.annotate("", xy=(-0.55, ax.get_ylim()[1] - 0.2), xytext=(-0.55, -0.4),
            arrowprops=dict(arrowstyle="-|>", lw=2.5, color="black"))

legend_handles = [
    Patch(facecolor=STEP_COLOR, edgecolor=STEP_COLOR, alpha=STEP_ALPHA,
          label="Computation step in a pipeline,\nsize indicates resource demand"),
    Patch(facecolor=NODE_COLOR, edgecolor=NODE_COLOR, alpha=NODE_ALPHA,
          label="Computer or “node” in a cluster"),
]
ax.legend(handles=legend_handles, loc="lower right", fontsize=11,
          frameon=False, bbox_to_anchor=(1.0, 0.0))

ax.set_aspect("equal")
plt.tight_layout()
plt.savefig(output_dir / "pipeline_figure.png", dpi=200)


#==================================================================================

# second figure - node 

# ---------------------------------------------------------------- settings
NODE_COLOR  = "grey"
NODE_ALPHA  = 0.55

# Matching colour palette: one colour per workflow / user.
USERS = ["Workflow A", "User B", "User C", "User D", "User E"]
COLORS = ["firebrick", "tab:orange", "tab:green", "tab:blue", "tab:purple"]
ALPHAS = [0.80, 0.70, 0.70, 0.65, 0.70]

NODE_W = NODE_H = 2.0                 # node size in node units
COL_GAP = 0.5                         # gap between nodes in a row
ROW_GAP = 1.4                         # vertical gap between time rows
PAD = 0.05                            # gap between and around small boxes

R, B, C, D, E = range(5)              # colour indices into COLORS

# ------------------------------------------------------- box layout utils
def blocks(x, y, w, h, cols, rows, ci):
    """Subdivide the rectangle into cols x rows rounded boxes of one user."""
    cw, ch = w / cols, h / rows
    out = []
    for i in range(cols):
        for j in range(rows):
            out.append((x + i * cw + PAD, y + j * ch + PAD,
                        cw - 2 * PAD, ch - 2 * PAD, ci))
    return out

def area(x, y, w, h, ci, cols=1, rows=1):
    """A region of the node filled with a grid of boxes of one user.

    cols x rows == number of boxes:
      1x1 = one big box, 1x2 = two mid-size boxes,
      2x4 (or 4x2) = 8 slightly bigger boxes, 4x4 = 16 small boxes.
    """
    return blocks(x, y, w, h, cols, rows, ci)

# Shorthand regions covering the whole node (with outer padding)
FULL = (PAD, PAD, NODE_W - 2 * PAD, NODE_H - 2 * PAD)
LHALF = (PAD, PAD, (NODE_W - 2 * PAD) / 2 - PAD / 2, NODE_H - 2 * PAD)
RHALF = (PAD + (NODE_W - 2 * PAD) / 2 + PAD / 2, PAD,
         (NODE_W - 2 * PAD) / 2 - PAD / 2, NODE_H - 2 * PAD)
TOP   = (PAD, PAD + (NODE_H - 2 * PAD) / 2 + PAD / 2,
         NODE_W - 2 * PAD, (NODE_H - 2 * PAD) / 2 - PAD / 2)
BOT   = (PAD, PAD, NODE_W - 2 * PAD, (NODE_H - 2 * PAD) / 2 - PAD / 2)

# ------------------------------------------------------- cluster contents
# 5 time rows, each a list of 5 nodes.
# A node is a list of `area(...)` calls; together they (partially) occupy
# the node. Workflow A (red) is the primary pipeline.

CLUSTER = [
    # ---- time row 0 (top): A ramps up on 2 nodes, others idle/partial
    [area(*FULL, R, 4, 4),                      # 16 small red boxes
     [],
     area(*BOT, B, 4, 2) + area(*TOP, C, 4, 2), # B bottom, C top
     [],
     []],
    # ---- time row 1: A takes whole nodes, rest mixed
    [area(*FULL, R, 1, 1),                      # one big red box
     area(*FULL, R, 1, 1),
     area(*RHALF, R, 1, 2) + area(*LHALF, D, 2, 4),
     area(*TOP, B, 1, 1) + area(*BOT, E, 4, 2),
     area(*LHALF, C, 1, 2) + area(*RHALF, B, 4, 4)],
    # ---- time row 2: busiest time
    [area(*FULL, R, 1, 1),
     area(*FULL, R, 1, 1),
     area(*FULL, R, 2, 2),                      # 8 slightly bigger red boxes
     area(*LHALF, R, 1, 4) + area(*RHALF, E, 1, 4),
     area(*TOP, C, 2, 4) + area(*BOT, B, 4, 2)],
    # ---- time row 3: A shrinks, mixed works
    [area(*FULL, R, 1, 1),
     area(*RHALF, R, 1, 2) + area(*LHALF, B, 2, 2),
     area(*FULL, R, 1, 1),
     area(*TOP, D, 1, 1) + area(*BOT, C, 4, 2),
     area(*FULL, E, 1, 1)],
    # ---- time row 4 (bottom): winding down, only leftovers
    [area(*TOP, R, 4, 2),
     area(*RHALF, R, 1, 4) + area(*LHALF, E, 1, 2),
     [],
     area(*BOT, B, 4, 2),
     area(*LHALF, D, 2, 2)],
]

# ------------------------------------------------------------------ draw
fig, ax = plt.subplots(figsize=(9.5, 12))

node_step_x = NODE_W + COL_GAP

def rounded(x, y, w, h, color, alpha, rs, lw=1.2):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={rs}",
        facecolor=color, edgecolor=color, alpha=alpha, linewidth=lw))

for r, row in enumerate(CLUSTER):
    y0 = r * (NODE_H + ROW_GAP)
    for n, node in enumerate(row):
        x0 = n * node_step_x
        rounded(x0, y0, NODE_W, NODE_H, NODE_COLOR, NODE_ALPHA, rs=0.18, lw=1.5)
        for (sx, sy, sw, sh, ci) in node:
            rounded(x0 + sx, y0 + sy, sw, sh, COLORS[ci], ALPHAS[ci], rs=min(0.08, sw/4, sh/4))

# ------------------------------------------------------- axes and legend
ax.set_xlim(-0.8, 5 * node_step_x)
ax.set_ylim(-0.6, 5 * (NODE_H + ROW_GAP) + 0.4)

ax.set_ylabel("Time (not linear)", fontsize=13)
ax.set_xticks([])
ax.set_yticks([])
for spine in ("top", "right", "bottom"):
    ax.spines[spine].set_visible(False)

ax.annotate("", xy=(-0.55, ax.get_ylim()[1]), xytext=(-0.55, -0.4),
            arrowprops=dict(arrowstyle="-|>", lw=2.5, color="black"))

legend_handles = [
    Patch(facecolor=c, edgecolor=c, alpha=a, label=u)
    for u, c, a in zip(USERS, COLORS, ALPHAS)
] + [
    Patch(facecolor=NODE_COLOR, edgecolor=NODE_COLOR, alpha=NODE_ALPHA,
          label="Computer or \u201cnode\u201d in a cluster"),
]
# Legend BELOW the axes: with bbox_inches="tight" it is saved fully and
# can never overlap the plot.
ax.legend(handles=legend_handles, loc="upper center", ncols=3,
          fontsize=11, frameon=False,
          bbox_to_anchor=(0.5, -0.01), borderaxespad=0)

ax.set_aspect("equal")
plt.savefig(output_dir / "cluster_utilization.png", dpi=200, bbox_inches="tight")
