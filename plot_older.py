"""Plot older gauges from BR manual"""
import matplotlib.pyplot as plt
import numpy as np

from plotting import make_rail_axes
from br20873 import BR20873_GAUGES
from plot_gauge import W6A_UPPER


def main():
    """Plot various gauges from a bygone era."""
    fig = plt.figure()
    # fig.patch.set_facecolor('xkcd:mint green')

    ax = fig.add_axes([0, 0, 1, 1])
    make_rail_axes(ax)

    for gauge in BR20873_GAUGES:
        gauge.plot(ax)

    topright = W6A_UPPER
    topleft = np.flipud(topright) * np.array([-1, 1])
    points = np.concat((topright, topleft))
    ax.plot(points[:, 0], points[:, 1], color="k")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
