"""
Unit and regression test for the molecool package.
"""

# Import package, test suite, and other packages as needed
import molecool
import pytest
import sys
import numpy as np

def test_molecool_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molecool" in sys.modules


def test_molecular_mass():
    symbols = ['C', 'H', 'H', 'H', 'H']

    calculated_mass = molecool.calculate_molecular_mass(symbols)

    actual_mass = 16.04

    assert pytest.approx(actual_mass, abs=1e-2) == calculated_mass

def test_calculate_angle():

    theta1 = np.array([0, 0, -1]) 
    theta2 = np.array([0, 0, 0])
    theta3 = np.array([1, 0, 0]) 

    expected_angle = 90

    calculated_angle = molecool.calculate_angle(theta1, theta2, theta3, degrees=True)

    assert expected_angle == calculated_angle