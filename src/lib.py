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

