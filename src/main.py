from lib import (
    Arm,
    Effector,
    arm_to_homogenous_matrix,
    get_homogenous_matrix_from_len_angle,
    mul_homogenous_matrixes,
    rot2d,
)

ARMS_NO_PER_SIDE = 5
ARM_LEN = 0.04


def main():
    # Checar bien los lados !!

    # Definition of left side
    left_side_arms: list[Arm] = []
    left_side_arm_angles = [30, 30, -55, -30, 25]

    for theta in left_side_arm_angles:
        left_side_arms.append(Arm(length=ARMS_NO_PER_SIDE, theta=theta))

    # End effecto
    l_effector = Effector(dx=0.01, dy=0.25, theta=left_side_arm_angles[-1])
    left_side_arms[-1] = l_effector.to_arm()

    l_homogeneous_m = [arm_to_homogenous_matrix(arm) for arm in left_side_arms]

    print("Matrixes")
    for idx, m in enumerate(l_homogeneous_m):
        print(f"M{idx + 1}")
        print(m)
        pass

    print("Final matrix")
    T_L_5 = mul_homogenous_matrixes(l_homogeneous_m)

    print(T_L_5)

    # # Definition of left side
    # left_side: list[Arm] = []

    # left_side: list[Arm] = []
    # left_side_thetas = [30, 30, -55, -30, 25]

    # for theta in left_side_thetas:
    #     left_side.append(Arm(length=ARMS_NO_PER_SIDE, theta=180 - theta))

    # # Last theta is with correct orientation
    # l_effector = Effector(theta=left_side_thetas[-1], dx=0.01, dy=0.25)
    # # todo: check if this is correct, i think is not
    # left_side[-1] = l_effector.to_arm()

    # assert len(left_side) == len(
    #     right_side
    # ), "Sides do not have \
    #         the same number of arms"

    # for arms in zip(right_side, left_side):
    #     for a in arms:
    #         print(a)


if __name__ == "__main__":
    main()
