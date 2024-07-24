from matplotlib import pyplot as plt
import numpy as np


def activity_plot(data, xticks=None, yticks=None):
    fig, ax = plt.subplots(figsize=(8, 1.5))
    ax.pcolormesh(data, vmin=0, vmax=5, cmap="Blues", edgecolors="white")
    ax.set_xticks(np.arange(len(xticks)), labels=xticks)
    ax.set_yticks(np.arange(len(yticks)), labels=yticks)
    ax.spines['bottom'].set_color("white")
    ax.spines['top'].set_color("white")
    ax.spines['right'].set_color("white")
    ax.spines['left'].set_color("white")
    ax.tick_params(axis="x", color="white")
    ax.tick_params(axis="y", color="white")
    ax.grid(color="w", linestyle="-", linewidth=1)
    ax.set_aspect("equal")
    ax.yaxis.set_ticks_position("right")
    fig.tight_layout()
    return fig
