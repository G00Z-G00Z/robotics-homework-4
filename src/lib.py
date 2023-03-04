"""
Author: Eduardo Gomez
"""
from functools import reduce

import numpy as np
from numpy import ndarray


def rot2d(theta: float) -> ndarray:
    """Rotation matrix in 2 dimensions"""
    theta = np.deg2rad(theta)
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])


def get_arm_end_coordinates(length: float, angle: float):
    """
    Returns a 2d vector with a final position
    """
    angle = np.deg2rad(angle)
    return np.array([np.cos(angle), np.sin(angle)]) * length


def get_homogenous_matrix_rt(rotation: ndarray, translation: ndarray) -> ndarray:
    """
    Gets homogeneous matrix from rotation and translation matrixes in 2d
    """
    translation = np.reshape(translation, (2, 1))
    return np.block([[rotation, translation], [np.zeros((1, 2)), 1]])


def mul_homogenous_matrixes(transform_matrices: list[ndarray]) -> ndarray:
    """
    Multiplies a list of homogeneous matrixes, from right to left
    """
    return reduce(lambda prev, next: next @ prev, transform_matrices[::-1])
