"""
Tests for functionality checks in class SolveDiffusion2D
"""
import unittest
import numpy as np
import pytest
from unittest import TestCase

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    # Fixture
    w=30. 
    h=20.
    dx=0.2
    dy=0.5

    d=3.5
    T_cold=200.
    T_hot=600.

    # Expected result
    dt= 0.0049

    # Actual result
    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)
    actual_dt = pytest.approx(solver.dt, 0.01)

    # Test
    assert actual_dt == dt


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    # Fixture
    w=1. 
    h=2.
    dx=0.2
    dy=0.5

    d=3.5
    T_cold=300.
    T_hot=600.

    # Expected result
    u= np.array([[300., 300., 300., 300.],
                 [300., 300., 300., 300.],
                 [300., 300., 300., 300.],
                 [300., 300., 300., 300.],
                 [300., 300., 300., 300.]])

    # Actual result
    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)
    actual_u = solver.set_initial_condition()

    # Test
    assert actual_u.shape == u.shape
    
    assert np.allclose(actual_u, u, 20)
