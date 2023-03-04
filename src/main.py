from lib import (
    get_arm_end_coordinates,
    get_homogenous_matrix_rt,
    mul_homogenous_matrixes,
    rot2d,
)
import numpy as np

ARMS_NO_PER_SIDE = 5
ARM_LEN = 4

# Local origin vector, which is all 0
LOCAL_ORIGIN_VEC = np.array([0, 0, 1])


def main():
    # Definition of left side
    # ls = left-side
    ls_arm_angles = [30, 30, -55, -30, 25]
    ls_arm_local_positions = [
        get_arm_end_coordinates(ARM_LEN, angle) for angle in ls_arm_angles[0:-1]
    ]

    # Effector coordinates
    ls_arm_local_positions.append(np.array([1, 0.25]))

    ls_homogeneous_m = [
        get_homogenous_matrix_rt(rot2d(angle), translation)
        for angle, translation in zip(ls_arm_angles, ls_arm_local_positions)
    ]

    T_L_5 = mul_homogenous_matrixes(ls_homogeneous_m)
    print(T_L_5)
    print(T_L_5 @ LOCAL_ORIGIN_VEC)

    # Definition of right side
    # rs = right-side

    rs_arm_angles = [30, 30, -55, -30, 25]

    # Adjust the angle by 180 - angle, to put the arm in the correct coordinate
    rs_arm_local_positions = [
        get_arm_end_coordinates(ARM_LEN, 180 - angle) for angle in rs_arm_angles[0:-1]
    ]

    # Effector coordinates
    rs_arm_local_positions.append(np.array([-1, 0.25]))

    # The angle is negative, to rotate the plane in the correct direction
    # The way to see it, is in respect to the x-axis of the prev plane
    rs_homogeneous_m = [
        get_homogenous_matrix_rt(rot2d(-angle), translation)
        for angle, translation in zip(rs_arm_angles, rs_arm_local_positions)
    ]

    T_L_10 = mul_homogenous_matrixes(rs_homogeneous_m)
    print(T_L_10)
    print(T_L_10 @ LOCAL_ORIGIN_VEC)

    # Rotation matrix to the right arm, in respect with left

    # Only is a translation in the x direction
    TLR = get_homogenous_matrix_rt(rot2d(0), np.array([41.5, 0]))
    print(TLR)
    print(TLR @ LOCAL_ORIGIN_VEC)


if __name__ == "__main__":
    main()
