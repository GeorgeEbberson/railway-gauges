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


class Gauge:

    def __init__(self, name, points):
        """Construct an instance."""
        self.name = name
        self.points = np.array(points)


class CubicSplineGauge(Gauge):
    """Gauge whose top follows a curve, which will be cubic spline fitted."""

    def plot(self, ax):
        """Draw the gauge on ax."""
        sdata = self.points.copy()
        sdata[:, [0, 1]] = sdata[:, [1, 0]]
        sdata[:, 0] *= -0.5
        points = np.concat((sdata, np.flipud(sdata[:-1, :] * np.array([-1, 1]))))

        cs = CubicSpline(points[:, 0], points[:, 1])
        xs = np.linspace(np.min(points[:, 0]), np.max(points[:, 0]), 50)
        x_vals = np.concat(([xs[0]], xs, [xs[-1]]))
        y_vals = np.concat(([0], cs(xs), [0]))
        if self.name == "BR20873_52":
            ax.plot(x_vals, y_vals, label=self.name)


class LinearGauge(Gauge):
    """Gauge defined by straight line joining points."""

    def plot(self, ax):
        """Draw gauge on ax."""
        sdata = self.points.copy()
        sdata[:, [0, 1]] = sdata[:, [1, 0]]
        sdata[:, 0] *= -0.5
        points = np.concat((sdata, np.flipud(sdata * np.array([-1, 1]))))

        x_vals = np.concat(([points[0, 0]], points[:, 0], [points[-1, 0]]))
        y_vals = np.concat(([0], points[:, 1], [0]))
        # ax.plot(x_vals, y_vals, label=self.name)


class TruncatedGauge(Gauge):
    """Gauge defined by a continuous curve then flat bit on top."""

    def plot(self, ax):
        """Draw gauge on ax."""
        # Treat it just like a CubicSpline except we then only draw the two sides.
        sdata = self.points.copy()
        sdata[:, [0, 1]] = sdata[:, [1, 0]]
        sdata[:, 0] *= -0.5
        points = np.concat((sdata, np.flipud(sdata * np.array([-1, 1]))))

        cs = CubicSpline(points[:, 0], points[:, 1])

        xs1 = np.linspace(self.points[0, 1], self.points[-1, 1], 50) * -0.5
        xs = np.concat((xs1, -1 * xs1[::-1]))
        x_vals = np.concat(([xs[0]], xs, [xs[-1]]))
        y_vals = np.concat(([0], cs(xs), [0]))
        # ax.plot(x_vals, y_vals, label=self.name)


class LiftedGauge(Gauge):
    """Gauge where there is a flat-topped step in the middle."""

    def __init__(self, *args, **kwargs):
        self.curve_top_height = kwargs.pop("curve_top_height")
        super().__init__(*args, **kwargs)

    def plot(self, ax):
        """Draw gauge on ax."""
        # Treat it just like a CubicSpline except we then only draw the two sides.
        sdata = self.points[:-1, :].copy()  # Last row not in spline data
        sdata = np.append(sdata, [[self.curve_top_height, 0]], axis=0)
        sdata[:, [0, 1]] = sdata[:, [1, 0]]
        sdata[:, 0] *= -0.5
        points = np.concat((sdata, np.flipud(sdata[:-1, :] * np.array([-1, 1]))))

        cs = CubicSpline(points[:, 0], points[:, 1])

        height = self.points[-1, 0]
        xs1 = np.linspace(self.points[0, 1], self.points[-1, 1], 50) * -0.5
        xs2 = -1 * xs1[::-1]
        x_vals = np.concat(([xs1[0]], xs1, [xs1[-1], xs2[0]], xs2, [xs2[-1]]))
        y_vals = np.concat(([0], cs(xs1), [height, height], cs(xs2), [0]))
        # ax.plot(x_vals, y_vals, label=self.name)
