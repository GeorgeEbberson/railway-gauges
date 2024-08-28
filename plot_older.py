"""Plot older gauges from BR manual"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

from axes import make_rail_axes
from br20873 import *
from plot_gauge import W6A_UPPER


def plot_cubicspline_roof(ax, sdata, **kwargs):
    """Plot a simple gauge with a cubic spline roof.

    sdata is the height and the total width at that height.
    """
    sdata[:, [0, 1]] = sdata[:, [1, 0]]
    sdata[:, 0] *= -0.5
    points = np.concat((sdata, np.flipud(sdata[:-1, :] * np.array([-1, 1]))))

    cs = CubicSpline(points[:, 0], points[:, 1])
    xs = np.linspace(np.min(points[:, 0]), np.max(points[:, 0]), 50)
    x_vals = np.concat(([xs[0]], xs, [xs[-1]]))
    y_vals = np.concat(([0], cs(xs), [0]))
    ax.plot(x_vals, y_vals, **kwargs)


def plot_square_roof(ax, sdata, **kwargs):
    """Plot a simple gauge with a square roof.

    sdata is the height and width at that height.
    """
    corners = np.array([
        [-sdata[0, 1]/2, 0],
        [-sdata[0, 1]/2, sdata[0, 0]],
        [sdata[0, 1]/2, sdata[0, 0]],
        [sdata[0, 1]/2, 0],
    ])
    ax.plot(corners[:, 0], corners[:, 1], **kwargs)


DATA = {
    "1": (plot_cubicspline_roof, BR20873_1),
    "2": (plot_cubicspline_roof, BR20873_2),
    # 3
    "4": (plot_cubicspline_roof, BR20873_4),
    "5": (plot_cubicspline_roof, BR20873_5),
    "6": (plot_cubicspline_roof, BR20873_6),
    "7": (plot_cubicspline_roof, BR20873_7),
    "8": (plot_cubicspline_roof, BR20873_8),
    "9": (plot_cubicspline_roof, BR20873_9),
    "10": (plot_cubicspline_roof, BR20873_10),
    # 11
    "12": (plot_cubicspline_roof, BR20873_12),
    # 13
    "14": (plot_cubicspline_roof, BR20873_14),
    "15": (plot_square_roof, BR20873_15),
    "16": (plot_cubicspline_roof, BR20873_16),
    "17": (plot_cubicspline_roof, BR20873_17),
    "18": (plot_cubicspline_roof, BR20873_18),
    # 19
    # 20
    "21": (plot_cubicspline_roof, BR20873_21),
    # 22
    "23": (plot_cubicspline_roof, BR20873_23),
    # 24
    "25": (plot_cubicspline_roof, BR20873_25),
    "26": (plot_cubicspline_roof, BR20873_26),
    # 27
    "28": (plot_cubicspline_roof, BR20873_28),
    # 29
    # 30
    # 31
    "32": (plot_cubicspline_roof, BR20873_32),
    # 33
    "34": (plot_cubicspline_roof, BR20873_34),
    # 35
    "36": (plot_cubicspline_roof, BR20873_36),
    "37": (plot_cubicspline_roof, BR20873_37),
    "38": (plot_cubicspline_roof, BR20873_38),
    # 39
    "40": (plot_cubicspline_roof, BR20873_40),
    "41": (plot_cubicspline_roof, BR20873_41),
    "42": (plot_cubicspline_roof, BR20873_42),
    # 43
    # 44
    "45": (plot_cubicspline_roof, BR20873_45),
    "46": (plot_cubicspline_roof, BR20873_46),
    "47": (plot_cubicspline_roof, BR20873_47),
    "48": (plot_cubicspline_roof, BR20873_48),
    "49": (plot_cubicspline_roof, BR20873_49),
    "50": (plot_cubicspline_roof, BR20873_50),
    "51": (plot_cubicspline_roof, BR20873_51),
    # 52
    "53": (plot_cubicspline_roof, BR20873_53),
    "54": (plot_cubicspline_roof, BR20873_54),
    "55": (plot_cubicspline_roof, BR20873_55),
    "56": (plot_cubicspline_roof, BR20873_56),
    # 57
    "58": (plot_cubicspline_roof, BR20873_58),
    # 59
    "60": (plot_cubicspline_roof, BR20873_60),
    "61": (plot_cubicspline_roof, BR20873_61),
    "62": (plot_cubicspline_roof, BR20873_62),
    "63": (plot_cubicspline_roof, BR20873_63),
    "64": (plot_cubicspline_roof, BR20873_64),
    # 65
    "66": (plot_cubicspline_roof, BR20873_66),
    "67": (plot_cubicspline_roof, BR20873_67),
    "68": (plot_cubicspline_roof, BR20873_68),
    "69": (plot_cubicspline_roof, BR20873_69),
    "70": (plot_cubicspline_roof, BR20873_70),
    "71": (plot_cubicspline_roof, BR20873_71),
    "72": (plot_cubicspline_roof, BR20873_72),
    "73": (plot_cubicspline_roof, BR20873_73),
    "74": (plot_cubicspline_roof, BR20873_74),
    "75": (plot_cubicspline_roof, BR20873_75),
    "76": (plot_cubicspline_roof, BR20873_76),
    "77": (plot_cubicspline_roof, BR20873_77),
    "78": (plot_cubicspline_roof, BR20873_78),
    # 79
}


def main():
    """Plot various gauges from a bygone era."""
    fig = plt.figure()
    # fig.patch.set_facecolor('xkcd:mint green')

    ax = fig.add_axes([0, 0, 1, 1])
    make_rail_axes(ax)

    for label, (func, data) in DATA.items():
        func(ax, np.array(data), label=label)

    topright = W6A_UPPER
    topleft = np.flipud(topright) * np.array([-1, 1])
    points = np.concat((topright, topleft))
    ax.plot(points[:, 0], points[:, 1], color="k")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
