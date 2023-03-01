from lib import Arm, Effector, get_homogenous_matrix_from_len_angle, rot2d

ARMS_NO_PER_SIDE = 5
ARM_LEN = 0.04


def main():
    # Definition of right side
    right_side: list[Arm] = []
    right_side_thetas = [30, 30, -55, -30, 25]

    for theta in right_side_thetas:
        right_side.append(Arm(length=ARMS_NO_PER_SIDE, theta=theta))

    # Last View effector
    r_effector = Effector(theta=right_side_thetas[-1], dx=0.01, dy=0.25)
    right_side[-1] = r_effector.to_arm()

    # Definition of left side
    left_side: list[Arm] = []

    left_side: list[Arm] = []
    left_side_thetas = [30, 30, -55, -30, 25]

    for theta in left_side_thetas:
        left_side.append(Arm(length=ARMS_NO_PER_SIDE, theta=180 - theta))

    # Last theta is with correct orientation
    l_effector = Effector(theta=left_side_thetas[-1], dx=0.01, dy=0.25)
    left_side[-1] = l_effector.to_arm()

    assert len(left_side) == len(
        right_side
    ), "Sides do not have \
            the same number of arms"

    for arms in zip(right_side, left_side):
        for a in arms:
            print(a)


if __name__ == "__main__":
    main()
