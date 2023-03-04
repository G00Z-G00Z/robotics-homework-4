from lib import (
    get_arm_end_coordinates,
    get_homogenous_matrix_rt,
    mul_homogenous_matrixes,
    rot2d,
)
import numpy as np

ARMS_NO_PER_SIDE = 5
ARM_LEN = 4


def main():
    # Checar bien los lados !!

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
    print(T_L_5 @ np.array([0, 0, 1]))


if __name__ == "__main__":
    main()
