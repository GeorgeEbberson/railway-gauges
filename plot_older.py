"""Plot older gauges from BR manual"""
import matplotlib.pyplot as plt
import numpy as np

from plotting import make_rail_axes
from br20873 import BR20873_GAUGES
from plot_gauge import W6A_UPPER
from units import ft


def plot_grid(ax):
    """Plot a faint grid."""
    for y_ft in range(15):
        y_val = ft(y_ft)
        ax.axhline(y_val, color=[0.95] * 3, zorder=0)
        ax.text(ft(6.5), y_val, f"{y_ft} ft", ha="center", va="center", color=[0.7] * 3, backgroundcolor="white", zorder=1)
    for x in range(-10, 10):
        ax.axvline(ft(x), color=[0.95] * 3, zorder=0)


def main():
    """Plot various gauges from a bygone era."""
    fig = plt.figure(figsize=(14, 9))

    ax = fig.add_axes([0, 0, 1, 1])
    make_rail_axes(ax, origin=False)
    plot_grid(ax)

    for gauge in BR20873_GAUGES:
        gauge.plot(ax)

    topright = W6A_UPPER
    topleft = np.flipud(topright) * np.array([-1, 1])
    points = np.concat((topright, topleft))
    ax.plot(points[:, 0], points[:, 1], color="r", linewidth=3, zorder=100)
    plt.show()


if __name__ == "__main__":
    main()
