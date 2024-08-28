"""Plot rails and a set of axes."""
import numpy as np


def plot_rail(ax, x=0, y=0):
    """Load the data and plot it."""
    data = np.genfromtxt("point_data/60e1_rail_points.csv", dtype=np.float64, delimiter=",")
    ax.fill(data[:, 0] + x, data[:, 1] + y, color="k")


def make_rail_axes(ax):
    """Add two rails and some lines to an axes."""
    ax.set_aspect("equal", adjustable="datalim")
    ax.axis("off")
    plot_rail(ax, x=-1435/2, y=-86)
    plot_rail(ax, x=1435/2, y=-86)
    ax.axvline(0, linestyle="-.", color="k")
    ax.axhline(0, linestyle=":", color="k", linewidth=0.5)
