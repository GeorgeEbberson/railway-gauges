"""Data gathered from B.R. 20873."""
from plotting import LiftedGauge, CubicSplineGauge, LinearGauge, TruncatedGauge
from units import ft


BR20873_GAUGES = (
    CubicSplineGauge("BR20873_1", (
        (ft(10, 5), ft(9, 3)),
        (ft(11, 5), ft(8, 0)),
        (ft(12, 5), ft(6, 0)),
        (ft(13, 5), 0),
    )),
    CubicSplineGauge("BR20873_2", (
        (ft(10, 3), ft(9, 3)),
        (ft(11, 3), ft(8, 3 + 1/32)),
        (ft(12, 3), ft(6, 6 + 5/8)),
        (ft(13, 3), ft(3, 1 + 5/32)),
        (ft(13, 6), 0),
    )),
    LiftedGauge("BR20873_3", (
        (ft(11, 0), ft(9, 0)),
        (ft(12, 0), ft(6, 8)),
        (ft(13, 1), ft(2, 0)),
    ), curve_top_height=ft(13, 0)),
    CubicSplineGauge("BR20873_4", (
        (ft(10, 9), ft(9, 3)),
        (ft(11, 9), ft(8, 1/8)),
        (ft(12, 9), ft(5, 11 + 1/4)),
        (ft(13, 9), 0),
    )),
    CubicSplineGauge("BR20873_5", (
        (ft(10, 9), ft(9, 3)),
        (ft(11, 9), ft(7, 10 + 1/4)),
        (ft(12, 9), ft(5, 5 + 1/2)),
        (ft(13, 6), 0),
    )),
    CubicSplineGauge("BR20873_6", (
        (ft(11, 0), ft(9, 3)),
        (ft(12, 0), ft(7, 10 + 3/32)),
        (ft(13, 0), ft(5, 5)),
        (ft(13, 9), 0),
    )),
    CubicSplineGauge("BR20873_7", (
        (ft(11, 0), ft(9, 0)),
        (ft(12, 0), ft(7, 4 + 5/8)),
        (ft(13, 0), ft(4, 5 + 15/16)),
        (ft(13, 6), 0),
    )),
    CubicSplineGauge("BR20873_8", (
        (ft(10, 9), ft(9, 0)),
        (ft(11, 9), ft(6, 11 + 1/2)),
        (ft(12, 9), ft(4, 11)),
        (ft(13, 9), 0),
    )),
    CubicSplineGauge("BR20873_9", (
        (ft(10, 9), ft(9, 3)),
        (ft(11, 9), ft(8, 3/4)),
        (ft(12, 9), ft(6, 1/2)),
        (ft(13, 9), 0),
    )),
    CubicSplineGauge("BR20873_10", (
        (ft(11, 0), ft(9, 0)),
        (ft(12, 0), ft(6, 8)),
        (ft(13, 0), 0),
    )),
    TruncatedGauge("BR20873_11", (
        (ft(11, 0), ft(9, 0)),
        (ft(12, 0), ft(7, 4 + 11/16)),
        (ft(13, 0), ft(4, 5 + 15/16)),
    )),
    CubicSplineGauge("BR20873_12", (
        (ft(11, 0), ft(9, 0)),
        (ft(12, 0), ft(7, 7/8)),
        (ft(13, 0), ft(3, 3 + 3/4)),
        (ft(13, 3), 0),
    )),
    LinearGauge("BR20873_13", (
        (ft(10, 3), ft(9, 0)),
        (ft(11, 3), ft(7, 2)),
        (ft(12, 3), ft(5, 4)),
        (ft(13, 3), ft(3, 6)),
    )),
    CubicSplineGauge("BR20873_14", (
        (ft(10, 11), ft(9, 0)),
        (ft(11, 11), ft(7, 2 + 1/8)),
        (ft(12, 11), ft(3, 9 + 1/4)),
        (ft(13, 3), 0),
    )),
    LinearGauge("BR20873_15", (
        (ft(11, 0), ft(9, 0)),
    )),
    CubicSplineGauge("BR20873_16", (
        (ft(10, 3), ft(9, 0)),
        (ft(11, 0), ft(8, 2)),
        (ft(12, 0), ft(6, 4)),
        (ft(13, 2), ft(3, 8 + 3/4)),
        (ft(13, 6), 0),
    )),
    CubicSplineGauge("BR20873_17", (
        (ft(11, 0), ft(8, 10)),
        (ft(12, 0), ft(7, 3 + 1/8)),
        (ft(13, 0), ft(4, 5 + 1/6)),
        (ft(13, 6), 0),
    )),
    CubicSplineGauge("BR20873_18", (
        (ft(10, 3), ft(8, 0)),
        (ft(11, 3), ft(6, 11)),
        (ft(12, 3), ft(4, 10 + 3/16)),
        (ft(13, 0), 0),
    )),
    LinearGauge("BR20873_19", (
        (ft(10, 9), ft(9, 0)),
        (ft(12, 0), ft(6, 5 + 3/8)),
    )),
    LinearGauge("BR20873_20", (
        (ft(10, 9), ft(9, 0)),
        (ft(11, 9), ft(6, 11 + 1/2)),
        (ft(12, 9), ft(4, 11)),
        (ft(13, 0), ft(4, 4 + 1/8)),
    )),
    CubicSplineGauge("BR20873_21", (
        (ft(10, 9), ft(7, 7)),
        (ft(11, 9), ft(5, 10 + 1/4)),
        (ft(12, 10), 0),
    )),
    LinearGauge("BR20873_22", (
        (ft(10, 6), ft(9, 0)),
        (ft(12, 2 + 1/4), ft(6, 1)),
        (ft(12, 9), ft(3, 5)),
    )),
    CubicSplineGauge("BR20873_23", (
        (ft(10, 6), ft(9, 0)),
        (ft(11, 10 + 1/2), ft(6, 2)),
        (ft(12, 6), 0),
    )),
    LiftedGauge("BR20873_24", (
        (ft(11, 0), ft(9, 0)),
        (ft(12, 0), ft(6, 8)),
        (ft(13, 2), ft(2, 8)),
    ), curve_top_height=ft(13, 0)),
    CubicSplineGauge("BR20873_25", (
        (ft(11, 1), ft(9, 0)),
        (ft(12, 1), ft(7, 3 + 1/2)),
        (ft(13, 1), ft(4, 2)),
        (ft(13, 6), 0),
    )),
    CubicSplineGauge("BR20873_26", (
        (ft(10, 11), ft(9, 0)),
        (ft(11, 11), ft(6, 11 + 1/2)),
        (ft(12, 11), ft(2, 9)),
        (ft(13, 1), 0),
    )),
    LinearGauge("BR20873_27", (
        (ft(10, 2), ft(9, 0)),
        (ft(11, 0), ft(8, 2)),
        (ft(12, 3), ft(5, 4)),
        (ft(12, 8), ft(3, 7)),
    )),
    CubicSplineGauge("BR20873_28", (
        (ft(12, 0), ft(9, 0)),
        (ft(13, 0), ft(5, 11 + 1/16)),
        (ft(13, 8), 0),
    )),
    LinearGauge("BR20873_29", (
        (ft(11, 6), ft(9, 0)),
        (ft(12, 6), ft(6, 9)),
        (ft(13, 6), ft(4, 6)),
    )),
    LinearGauge("BR20873_30", (
        (ft(11, 0), ft(9, 0)),
        (ft(11, 8), ft(8, 3/16)),
    )),
    TruncatedGauge("BR20873_31", (
        (ft(11, 0), ft(9, 0)),
        (ft(12, 0), ft(7, 4 + 11/16)),
        (ft(13, 0), ft(4, 5 + 15/16)),
        (ft(13, 3), ft(3, 2 + 1/2)),
    )),
    CubicSplineGauge("BR20873_32", (
        (ft(10, 10), ft(9, 0)),
        (ft(11, 10), ft(7, 4 + 11/16)),
        (ft(12, 10), ft(4, 5 + 15/16)),
        (ft(13, 4), 0),
    )),
    TruncatedGauge("BR20873_33", (
        (ft(11, 0), ft(9, 0)),
        (ft(12, 0), ft(7, 4 + 11/16)),
        (ft(13, 0), ft(4, 5 + 14/16)),
        (ft(13, 4), ft(2, 7 + 11/16)),
    )),
    CubicSplineGauge("BR20873_34", (
        (ft(10, 4), ft(9, 3)),
        (ft(11, 4), ft(8, 3 + 13/16)),
        (ft(12, 4), ft(5, 8 + 3/8)),
        (ft(13, 4), ft(3, 6 + 1/2)),
        (ft(13, 8), 0),
    )),
    TruncatedGauge("BR20873_35", (
        (ft(9, 10), ft(9, 8)),
        (ft(11, 3/8), ft(9, 0)),
        (ft(12, 0), ft(7, 2)),
        (ft(13, 0), ft(4, 4)),
        (ft(13, 6), ft(1, 6)),
    )),
    CubicSplineGauge("BR20873_36", (
        (ft(10, 1), ft(9, 3)),
        (ft(11, 1), ft(8, 3 + 13/16)),
        (ft(12, 1), ft(6, 8 + 3/8)),
        (ft(13, 1), ft(3, 6 + 1/2)),
        (ft(13, 5), 0),
    )),
    CubicSplineGauge("BR20873_37", (
        (ft(10, 9), ft(9, 0)),
        (ft(11, 9), ft(7, 7 + 13/16)),
        (ft(12, 9), ft(5, 3 + 9/16)),
        (ft(13, 6), 0),
    )),
    CubicSplineGauge("BR20873_38", (
        (ft(11, 6), ft(9, 0)),
        (ft(12, 6), ft(6, 1 + 11/16)),
        (ft(13, 3), 0),
    )),
    CubicSplineGauge("BR20873_40", (
        (ft(9, 8), ft(8, 0)),
        (ft(10, 8), 0),
    )),
    CubicSplineGauge("BR20873_41", (
        (ft(10, 9), ft(9, 0)),
        (ft(11, 9), ft(6, 11 + 3/16)),
        (ft(12, 9), ft(2, 9)),
        (ft(12, 11), 0),
    )),
    CubicSplineGauge("BR20873_42", (
        (ft(10, 6), ft(9, 0)),
        (ft(11, 6), ft(6, 4)),
        (ft(12, 4 + 1/2), 0),
    )),
    TruncatedGauge("BR20873_43", (
        (ft(10, 6), ft(9, 0)),
        (ft(11, 6), ft(7, 10 + 3/4)),
        (ft(12, 8), ft(3, 5 + 1/4)),
    )),
    LiftedGauge("BR20873_44", (
        (ft(10, 6), ft(9, 0)),
        (ft(11, 9 + 1/2), ft(6, 11 + 3/4)),
        (ft(13, 1), ft(1, 0)),
    ), curve_top_height=ft(13, 0)),
    CubicSplineGauge("BR20873_45", (
        (ft(11, 3), ft(9, 0)),
        (ft(12, 3), ft(5, 1 + 3/4)),
        (ft(13, 0), 0),
    )),
    CubicSplineGauge("BR20873_46", (
        (ft(10, 3), ft(8, 0)),
        (ft(11, 3), ft(6, 10)),
        (ft(12, 3), ft(4, 7 + 7/16)),
        (ft(12, 11), 0),
    )),
    CubicSplineGauge("BR20873_47", (
        (ft(10, 9), ft(9, 0)),
        (ft(11, 9), ft(5, 4 + 5/8)),
        (ft(12, 3), 0),
    )),
    CubicSplineGauge("BR20873_48", (
        (ft(10, 9), ft(8, 1)),
        (ft(11, 1), 0),
    )),
    CubicSplineGauge("BR20873_49", (
        (ft(10, 9), ft(9, 0)),
        (ft(11, 2), 0),
    )),
    CubicSplineGauge("BR20873_50", (
        (ft(10, 6), ft(9, 0)),
        (ft(11, 6), ft(7, 15/16)),
        (ft(12, 6), ft(3, 3 + 1/4)),
        (ft(12, 9), 0),
    )),
    CubicSplineGauge("BR20873_51", (
        (ft(10, 3), ft(9, 0)),
        (ft(11, 3), ft(8, 3/4)),
        (ft(12, 3), ft(6, 5)),
        (ft(13, 3), ft(3, 1/2)),
        (ft(13, 6), 0),
    )),
    CubicSplineGauge("BR20873_53", (
        (ft(10, 10), ft(9, 3)),
        (ft(11, 10), ft(7, 7)),
        (ft(12, 10), ft(4, 8)),
        (ft(13, 4), 0),
    )),
    CubicSplineGauge("BR20873_54", (
        (ft(10, 8), ft(8, 6)),
        (ft(11, 8), ft(6, 11 + 1/4)),
        (ft(12, 8), ft(3, 11 + 3/4)),
        (ft(13, 1), 0),
    )),
    CubicSplineGauge("BR20873_55", (
        (ft(10, 1 + 1/2), ft(9, 0)),
        (ft(11, 1 + 1/2), ft(7, 10 + 3/4)),
        (ft(12, 1 + 1/2), ft(4, 9 + 1/8)),
        (ft(12, 6), 0),
    )),
    CubicSplineGauge("BR20873_56", (
        (ft(8, 9), ft(9, 5)),
        (ft(9, 9), ft(6, 2 + 27/32)),
        (ft(10, 6), 0),
    )),
    TruncatedGauge("BR20873_57", (
        (ft(11, 0), ft(9, 0)),
        (ft(12, 0), ft(7, 4 + 1/2)),
        (ft(13, 1), ft(4, 1 + 1/2)),
    )),
    CubicSplineGauge("BR20873_58", (
        (ft(10, 3), ft(9, 3)),
        (ft(11, 3), ft(6, 11 + 1/2)),
        (ft(12, 4), 0),
    )),
    CubicSplineGauge("BR20873_60", (
        (ft(11, 0), ft(8, 6)),
        (ft(12, 0), ft(6, 9 + 3/4)),
        (ft(13, 0), ft(3, 7)),
        (ft(13, 4), 0),
    )),
    CubicSplineGauge("BR20873_61", (
        (ft(11, 0), ft(8, 6)),
        (ft(12, 0), ft(6, 3 + 3/4)),
        (ft(13, 0), 0),
    )),
    CubicSplineGauge("BR20873_62", (
        (ft(8, 3), ft(8, 6)),
        (ft(9, 0), 0),
    )),
    CubicSplineGauge("BR20873_63", (
        (ft(11, 0), ft(9, 0)),
        (ft(12, 0), ft(5, 11 + 3/4)),
        (ft(12, 8), 0),
    )),
    CubicSplineGauge("BR20873_64", (
        (ft(11, 0), ft(9, 0)),
        (ft(11, 11), 0),
    )),
    LinearGauge("BR20873_65", (
        (ft(10, 0), ft(8, 0)),
    )),
    CubicSplineGauge("BR20873_66", (
        (ft(10, 5), ft(9, 0)),
        (ft(11, 5), ft(5, 0)),
        (ft(11, 10), 0),
    )),
    CubicSplineGauge("BR20873_67", (
        (ft(11, 0), ft(9, 0)),
        (ft(12, 0), ft(6, 10)),
        (ft(13, 0), ft(2, 9 + 1/2)),
        (ft(13, 2), 0),
    )),
    CubicSplineGauge("BR20873_68", (
        (ft(11, 0), ft(9, 0)),
        (ft(12, 0), ft(5, 3 + 1/2)),
        (ft(12, 6), 0),
    )),
    CubicSplineGauge("BR20873_69", (
        (ft(11, 0), ft(9, 0)),
        (ft(12, 0), ft(7, 2 + 1/4)),
        (ft(13, 0), ft(3, 9 + 1/4)),
        (ft(13, 4), 0),
    )),
    CubicSplineGauge("BR20873_70", (
        (ft(10, 9), ft(9, 0)),
        (ft(11, 6), 0),
    )),
    CubicSplineGauge("BR20873_71", (
        (ft(10, 4), ft(9, 0)),
        (ft(11, 6), 0),
    )),
    CubicSplineGauge("BR20873_72", (
        (ft(9, 10), ft(9, 8)),
        (ft(10, 10), ft(8, 4 + 1/2)),
        (ft(11, 10), ft(6, 3)),
        (ft(12, 10), 0),
    )),
    CubicSplineGauge("BR20873_73", (
        (ft(10, 0), ft(9, 0)),
        (ft(11, 0), ft(7, 11 + 1/4)),
        (ft(12, 0), ft(5, 6 + 1/4)),
        (ft(12, 10), 0),
    )),
    CubicSplineGauge("BR20873_74", (
        (ft(9, 3), ft(9, 0)),
        (ft(10, 3), ft(7, 3/4)),
        (ft(11, 3), ft(3, 4)),
        (ft(11, 6), 0),
    )),
    CubicSplineGauge("BR20873_75", (
        (ft(11, 0), ft(9, 0)),
        (ft(12, 2), 0),
    )),
    CubicSplineGauge("BR20873_76", (
        (ft(11, 0), ft(8, 6)),
        (ft(12, 0), ft(7, 0)),
        (ft(13, 0), ft(4, 3 + 1/2)),
        (ft(13, 6), 0),
    )),
    CubicSplineGauge("BR20873_77", (
        (ft(10, 9), ft(8, 6)),
        (ft(11, 9), ft(6, 8 + 1/2)),
        (ft(12, 9), ft(3, 2)),
        (ft(13, 0), 0),
    )),
    CubicSplineGauge("BR20873_78", (
        (ft(11, 6), ft(9, 0)),
        (ft(12, 6), ft(5, 3 + 1/2)),
        (ft(13, 0), 0),
    )),
    LiftedGauge("BR20873_79", (
        (ft(11, 0), ft(9, 0)),
        (ft(12, 0), ft(6, 8)),
        (ft(13, 6), ft(2, 8)),
    ), curve_top_height=ft(13, 0)),
)
