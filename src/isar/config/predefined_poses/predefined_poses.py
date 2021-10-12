from models.geometry.frame import Frame
from models.geometry.orientation import Orientation
from models.geometry.pose import Pose
from models.geometry.position import Position

predefined_poses = {
    #
    # K-lab inlet area
    #
    "334-LD-0225": Pose(
        position=Position(x=1.63, y=1.724, z=0, frame=Frame.Robot),
        orientation=Orientation(x=0, y=0, z=0.5383686, w=0.8427095, frame=Frame.Robot),
        frame=Frame.Robot,
    ),
    "314-LD-1001": Pose(
        position=Position(x=24.853, y=23.761, z=0, frame=Frame.Robot),
        orientation=Orientation(x=0, y=0, z=0.998122, w=0.0612579, frame=Frame.Robot),
        frame=Frame.Robot,
    ),
    "346-LD-1073": Pose(
        position=Position(x=25.005, y=23.607, z=0, frame=Frame.Robot),
        orientation=Orientation(x=0, y=0, z=0.9995287, w=-0.0306988, frame=Frame.Robot),
        frame=Frame.Robot,
    ),
    "314-PI-001": Pose(
        position=Position(x=25.041, y=23.682, z=0, frame=Frame.Robot),
        orientation=Orientation(x=0, y=0, z=0.8907533, w=0.4544871, frame=Frame.Robot),
        frame=Frame.Robot,
    ),
    "300-LD-0025": Pose(
        position=Position(x=21.279, y=17.392, z=0, frame=Frame.Robot),
        orientation=Orientation(x=0, y=0, z=0.2006291, w=0.9796673, frame=Frame.Robot),
        frame=Frame.Robot,
    ),
    "344-LD-1001": Pose(
        position=Position(x=24.853, y=23.761, z=0, frame=Frame.Robot),
        orientation=Orientation(x=0, y=0, z=0.998122, w=0.0612579, frame=Frame.Robot),
        frame=Frame.Robot,
    ),
    "15-LD-0059": Pose(
        position=Position(x=27.297, y=22.686, z=0, frame=Frame.Robot),
        orientation=Orientation(x=0, y=0, z=0.9631559, w=0.2689439, frame=Frame.Robot),
        frame=Frame.Robot,
    ),
    "345-LD-1004": Pose(
        position=Position(x=20.293, y=20.982, z=0, frame=Frame.Robot),
        orientation=Orientation(x=0, y=0, z=0.5256679, w=0.8506899, frame=Frame.Robot),
        frame=Frame.Robot,
    ),
    # start of narrow passage
    "345-LD-003": Pose(
        position=Position(x=20.994, y=10.3, z=0, frame=Frame.Robot),
        orientation=Orientation(x=0, y=0, z=0.8963647, w=0.4433175, frame=Frame.Robot),
        frame=Frame.Robot,
    ),
    # end of narrow passage
    "345-LD-004": Pose(
        position=Position(x=16.609, y=15.444, z=0, frame=Frame.Robot),
        orientation=Orientation(x=0, y=0, z=0.999986, w=0.0052963, frame=Frame.Robot),
        frame=Frame.Robot,
    ),
    #
    # Compressor area K-lab
    #
    "355-LD-1003": Pose(
        position=Position(x=20248.440, y=5247.118, z=14.450, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=-0.054, w=0.998, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    "313-LD-1111": Pose(
        position=Position(x=20249.830, y=5246.737, z=14.450, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.999, w=-0.041, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # 313-LD-1104 and 313-PA-101A has the same pose
    "313-LD-1104": Pose(
        position=Position(x=20250.720, y=5252.582, z=14.450, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.356, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # 313-LD-1104 and 313-PA-101A has the same pose
    "313-PA-101A": Pose(
        position=Position(x=20252.860, y=5252.368, z=14.450, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    #
    #   Second Floor K-Lab Compressor area
    #
    # 300-LD-0066 and 300-XCV-003 has the same pose
    # Robot Orientation: 90 deg
    "300-LD-0066": Pose(
        position=Position(x=20259.220, y=5241.849, z=16.880, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # 300-LD-0066 and 300-XCV-003 has the same pose
    # Robot Orientation: 90 deg
    "300-XCV-003": Pose(
        position=Position(x=20259.220, y=5241.849, z=16.880, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # Robot Orientation: 0 deg
    "313-LD-1248": Pose(
        position=Position(x=20256.540, y=5243.902, z=16.880, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # Robot Orientation: 0 deg
    "313-FG-136": Pose(
        position=Position(x=20256.470, y=5243.299, z=16.880, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # 313-LD-1177 and 313-LD-1135 has the same pose
    # Robot Orientation: 270 deg
    "313-LD-1177": Pose(
        position=Position(x=20254.740, y=5242.001, z=16.880, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # 313-LD-1177 and 313-LD-1135 has the same pose
    # Robot Orientation: 270 deg
    "313-LD-1135": Pose(
        position=Position(x=20254.740, y=5242.001, z=16.880, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # Robot Orientation: 270 deg
    "313-LD-1133": Pose(
        position=Position(x=20252.960, y=5241.896, z=16.880, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # Robot Orientation: 270 deg
    "313-FG-135": Pose(
        position=Position(x=20252.100, y=5241.975, z=16.880, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # Robot Orientation: 90 deg
    "300-XCV-003": Pose(
        position=Position(x=20259.530, y=5241.897, z=16.880, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # 313-LD-1243 and 313-LD-1242 has the same pose
    # Robot Orientation: 180 deg
    "313-LD-1243": Pose(
        position=Position(x=20256.640, y=5243.246, z=16.880, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # 313-LD-1243 and 313-LD-1242 has the same pose
    # Robot Orientation: 180 deg
    "313-LD-1242": Pose(
        position=Position(x=20256.640, y=5243.246, z=16.880, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # Robot Orientation: 270 deg
    "313-LD-1037": Pose(
        position=Position(x=20254.650, y=5242.229, z=16.880, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # Robot Orientation: 270 deg
    "313-LD-1050": Pose(
        position=Position(x=20252.560, y=5241.928, z=16.880, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # Robot Orientation: 270 deg
    "313-TT-1102C": Pose(
        position=Position(x=20252.250, y=5242.033, z=16.880, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # 313-LD-1241 and 313-LD-1240 has the same pose
    # Robot Orientation: 270 deg
    "313-LD-1241": Pose(
        position=Position(x=20252.210, y=5241.930, z=16.880, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # 313-LD-1241 and 313-LD-1240 has the same pose
    # Robot Orientation: 270 deg
    "313-LD-1240": Pose(
        position=Position(x=20252.210, y=5241.930, z=16.880, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # Robot Orientation: 270 deg
    "313-LD-1056": Pose(
        position=Position(x=20256.470, y=5241.838, z=16.880, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # Robot Orientation: 270 deg
    "313-LD-1060": Pose(
        position=Position(x=20253.920, y=5246.332, z=16.880, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # Robot Orientation: 90 deg
    "313-PT-1012": Pose(
        position=Position(x=20252.940, y=5246.394, z=16.880, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # 313-PT-1061B and 313-LD-1257 has the same pose
    # Robot Orientation: 90 deg
    "313-PT-1016B": Pose(
        position=Position(x=20250.430, y=5246.008, z=16.880, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # 313-PT-1061B and 313-LD-1257 has the same pose
    # Robot Orientation: 90 deg
    "313-LD-1257": Pose(
        position=Position(x=20250.430, y=5246.008, z=16.880, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # 355-LD-1079 Robot orientation 90 degrees
    "355-LD-1079": Pose(
        position=Position(x=20252.630, y=5253.167, z=18.540, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # 331-EV-1009 Robot orientation 90 degrees
    "331-EV-1009": Pose(
        position=Position(x=20255.710, y=5252.991, z=18.540, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # 313-LD-1094 Robot orientation 90 degrees
    "313-LD-1094": Pose(
        position=Position(x=20255.710, y=5252.980, z=18.540, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # 313-LD-1095 Robot orientation 135 degrees
    "313-LD-1095": Pose(
        position=Position(x=20256.860, y=5252.572, z=18.540, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # 313-LD-1213 Robot orientation 180 degrees
    "313-LD-1213": Pose(
        position=Position(x=20257.070, y=5250.289, z=18.540, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # 313-LD-1214 Robot orientation 180 degrees
    "313-LD-1214": Pose(
        position=Position(x=20257.070, y=5250.289, z=18.540, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # 300-LD-1001 Robot orientation 235 degrees. Part above in 4th floor
    "300-LD-1001": Pose(
        position=Position(x=20257.000, y=5248.983, z=18.540, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # 300-LD-1002 Robot orientation 235 degrees. Part above in 4th floor
    "300-LD-1002": Pose(
        position=Position(x=20257.000, y=5248.983, z=18.540, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # 313-JA-001 Robot orientation 270 degrees
    "313-JA-001": Pose(
        position=Position(x=20255.810, y=5248.977, z=18.540, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # 313-HH-001 Robot orientation 0 degrees. Should have photo from other side?
    # Implementation of handling several photos for same part?
    "313-HH-001": Pose(
        position=Position(x=20250.810, y=5249.645, z=18.540, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # EJE-342-1004.08 Robot orientation 0 degrees
    "EJE-342-1004.08": Pose(
        position=Position(x=20251.050, y=5251.786, z=18.540, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # EJE-342-0226.10 Robot orientation 90 degrees
    "EJE-342-0226.10": Pose(
        position=Position(x=20252.070, y=5253.136, z=18.540, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # EJE-342-1004.03 Robot orientation 90 degrees
    "EJE-342-0226.10": Pose(
        position=Position(x=20252.630, y=5253.136, z=18.540, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # 313-KG-001 Robot orientation 90 degrees. Pose on stairs
    "313-KG-001": Pose(
        position=Position(x=20253.900, y=5253.020, z=18.735, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # JBZS-313-021 Robot orientation 270 degrees
    "JBZS-313-024": Pose(
        position=Position(x=20250.000, y=5253.155, z=18.540, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # JBZS-313-024 Robot orientation 315 degrees
    "JBZS-313-024": Pose(
        position=Position(x=20250.160, y=5249.555, z=18.540, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
    # JBES-313-003 Robot orientation 315 degrees
    "JBES-313-003": Pose(
        position=Position(x=20250.160, y=5249.555, z=18.540, frame=Frame.Asset),
        orientation=Orientation(x=0, y=0, z=0.935, w=0.357, frame=Frame.Asset),
        frame=Frame.Asset,
    ),
}