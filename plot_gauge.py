"""Plot railway gauge data"""
import matplotlib.pyplot as plt
import numpy as np

from axes import make_rail_axes

W6A_LOWER = np.array([
    [680, 75],  # 1D
    [680, 100],  # 2D
    [894, 100],  # 3D
    [894, 135],  # 4D
    [1037.5, 135],  # 5P
    [1350, 280],  # 6D
    [1350, 1000],  # 7D
])

W6A_UPPER = np.array([
    [1410, 1000],
    [1410, 3080],
    [1345, 3300],
    [1220, 3440],
    [795, 3750],
    [152.5, 3965],
])

W7_UPPER = np.array([
    [1410, 1000],
    [1410, 3080],
    [1345, 3300],
    [1240, 3418],
    [1240, 3531],
    [1095, 3531],
    [795, 3750],
    [152.5, 3965],
])

W8_UPPER = np.array([
    [1410, 1000],
    [1410, 3080],
    [1345, 3300],
    [1271, 3568],
    [1264, 3618],
    [976, 3618],
    [795, 3750],
    [152.5, 3965],
])

W8A_UPPER = np.array([
    [1321.5, 1000],
    [1321.5, 3300],
    [1262.5, 3512],
    [1262.5, 3635],
])

W9_UPPER = np.array([
    # First two only apply between bogeys, so not part of gauge really
    # [1312.5, 780],
    # [1312.5, 1000],
    [1398, 1000],
    [1398, 3080],
    [1333, 3300],
    [1312.5, 3323],
    [1312.5, 3695],
    [1262.5, 3701],
    [1262.5, 3715],
    [678, 3785],
    [140, 3965],
])

W9A_UPPER = np.array([
    [1312.5, 1000],
    [1312.5, 3730],
    [1125, 3730],
    [0, 3866],
])

W10_UPPER = np.array([
    [1262.5, 820],
    [1262.5, 3841],
    [1256, 3841],
    [1256, 3891],
])

W10A_UPPER = np.array([
    [1262.5, 820],
    [1262.5, 3891],
])

W12_UPPER = np.array([
    [1300, 700],
    [1300, 3841],
    [1275, 3841],
    [1275, 3896],
    [575, 3896],
    [0, 3965],
])


def draw_train(ax, lower, upper):
    """Given some upper and lower points, draw a train outline."""
    bottom_right = lower
    top_right = upper
    top_left = np.flipud(upper) * np.array([-1, 1])
    bottom_left = np.flipud(lower) * np.array([-1, 1])

    data = np.concat((bottom_right, top_right, top_left, bottom_left))
    ax.fill(data[:, 0], data[:, 1])


def main():
    """Plot stuff."""
    fig, axs = plt.subplots()
    make_rail_axes(axs)
    draw_train(axs, W6A_LOWER, W10A_UPPER)

    container = np.array([
        [1219, 3510],
        [-1219, 3510],
        [-1219, 1072],
        [1219, 1072],
        [1219, 3510],
    ])

    axs.plot(container[:, 0], container[:, 1], color="k")

    plt.show()


if __name__ == "__main__":
    main()