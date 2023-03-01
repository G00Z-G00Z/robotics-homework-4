"""
Author: Eduardo Gomez
"""
from dataclasses import dataclass
from functools import reduce

import numpy as np
from numpy import ndarray


@dataclass
class Arm:
    """Defines an arm metadata"""

    length: float = 0
    "Defines the rotation from the x axis in degrees"
    theta: float = 0


@dataclass
class Effector:
    """End effector"""

    dx: float = 0
    dy: float = 0
    theta: float = 0

    def to_arm(self) -> Arm:
        return Arm(length=np.sqrt(self.dx**2 + self.dy**2), theta=self.theta)


def rot2d(theta: float) -> ndarray:
    """Rotation matrix in 2 dimensions"""
    theta = np.deg2rad(theta)
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])


def get_homogenous_matrix_from_len_angle(angle: float, length: float) -> ndarray:
    """
    Gets the homogeneous matrix from angle and length
    """
    # Get the rotation matrix
    rot = rot2d(angle)

    # Get the coordinates of the end of the arm
    arm_length = np.array([length, 0])
    arm_length = np.reshape(arm_length, (2, 1))
    initial_position: ndarray = rot @ arm_length

    # Block puts the vectors or matrixes together as long as dimension match
    return np.block([[rot, initial_position], [np.zeros((1, 2)), 1]])


def solve_final_angle(arms: list[Arm]) -> ndarray:
    transform_matrices = [
        get_homogenous_matrix_from_len_angle(a.theta, a.length) for a in arms
    ]

    for idx, mat in enumerate(transform_matrices):
        print(f"T{idx + 1}: ")
        print(mat)

    final_matrix = reduce(lambda prev, next: next @ prev, transform_matrices[::-1])

    print("Final Matrix: ")
    print(final_matrix)
    print("Final Coord: ")
    coord = final_matrix[0:2, 2]
    print(final_matrix[0:2, 2])
    return coord


if __name__ == "__main__":
    arms_no = 3

    arms = [Arm() for _ in range(arms_no)]

    arms_length = 0.04

    arms[0].length = arms_length
    arms[0].theta = 30
    arms[1].length = arms_length
    arms[1].theta = 30
    arms[2].length = arms_length
    arms[2].theta = -55

    solve_final_angle(arms)
    pass
