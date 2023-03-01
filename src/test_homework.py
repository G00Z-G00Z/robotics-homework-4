import numpy as np
import pytest
from .lib import Arm, solve_final_angle, get_homogenous_matrix_from_len_angle


def _get_list_of_arms(how_many: int):
    return [Arm() for _ in range(how_many)]


def test_case_3_arms():
    arms = _get_list_of_arms(3)
    arms_length = 0.04

    arms[0].length = arms_length
    arms[0].theta = 30
    arms[1].length = arms_length
    arms[1].theta = 30
    arms[2].length = arms_length
    arms[2].theta = -55

    coord = solve_final_angle(arms)
    expected = [0.0944, 0.0581]
    assert np.allclose(
        coord.round(4), expected, atol=0.0001, rtol=0.1
    ), f"{coord.round(4)} != {expected}"


def test_case_4():
    arms = _get_list_of_arms(4)
    arms_length = 0.04
    arms[0].length = arms_length
    arms[0].theta = 30
    arms[1].length = arms_length
    arms[1].theta = 30
    arms[2].length = arms_length
    arms[2].theta = -55
    arms[3].length = arms_length
    arms[3].theta = -30
    coord = solve_final_angle(arms)
    expected = [0.1307, 0.0412]
    assert np.allclose(
        coord.round(4), expected, atol=0.0001, rtol=0.1
    ), f"{coord.round(4)} != {expected}"


def test_case_5():
    arms = _get_list_of_arms(5)
    arms_length = 0.04
    arms[0].length = arms_length
    arms[0].theta = 30
    arms[1].length = arms_length
    arms[1].theta = 30
    arms[2].length = arms_length
    arms[2].theta = -55
    arms[3].length = arms_length
    arms[3].theta = -30
    lidar_length = 0.05
    lidar_theta = -20
    arms[4].length = lidar_length
    arms[4].theta = lidar_theta
    coord = solve_final_angle(arms)
    expected = [0.1307, 0.0412]
    # assert np.allclose( coord.round(4), expected, atol=0.0001, rtol=0.1), f"{coord.round(4)} != {expected}"
