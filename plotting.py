"""Plot rails and a set of axes."""
import numpy as np
from scipy.interpolate import CubicSpline


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


class CubicSplineGauge:

    def __init__(self, name, points):
        """Construct an instance."""
        self.name = name
        self.points = np.array(points)

    def plot(self, ax, **kwargs):
        """Draw the gauge on ax."""
        sdata = self.points
        sdata[:, [0, 1]] = sdata[:, [1, 0]]
        sdata[:, 0] *= -0.5
        points = np.concat((sdata, np.flipud(sdata[:-1, :] * np.array([-1, 1]))))

        cs = CubicSpline(points[:, 0], points[:, 1])
        xs = np.linspace(np.min(points[:, 0]), np.max(points[:, 0]), 50)
        x_vals = np.concat(([xs[0]], xs, [xs[-1]]))
        y_vals = np.concat(([0], cs(xs), [0]))
        ax.plot(x_vals, y_vals, label=self.name, **kwargs)
