"""Plot older gauges from BR manual"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

from axes import make_rail_axes

MM_PER_IN = 25.4
IN_PER_FT = 12


def ft(feet=0, inches=0):
    """Millimetres from feet and inches."""
    return (feet * IN_PER_FT + inches) * MM_PER_IN


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


BR20873_1 = (
    (ft(10, 5), ft(9, 3)),
    (ft(11, 5), ft(8, 0)),
    (ft(12, 5), ft(6, 0)),
    (ft(13, 5), 0),
)

BR20873_2 = (
    (ft(10, 3), ft(9, 3)),
    (ft(11, 3), ft(8, 3 + 1/32)),
    (ft(12, 3), ft(6, 6 + 5/8)),
    (ft(13, 3), ft(3, 1 + 5/32)),
    (ft(13, 6), 0),
)

BR20873_4 = (
    (ft(10, 9), ft(9, 3)),
    (ft(11, 9), ft(8, 1/8)),
    (ft(12, 9), ft(5, 11 + 1/4)),
    (ft(13, 9), 0),
)


DATA = {
    "1": (plot_cubicspline_roof, BR20873_1),
    "2": (plot_cubicspline_roof, BR20873_2),
    "4": (plot_cubicspline_roof, BR20873_4),
}


def main():
    """Plot various gauges from a bygone era."""
    fig, ax = plt.subplots(nrows=1, ncols=1)
    make_rail_axes(ax)

    for label, (func, data) in DATA.items():
        func(ax, np.array(data), label=label)

    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
