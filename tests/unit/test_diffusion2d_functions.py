"""
Tests for functions in class SolveDiffusion2D
"""

import pytest
from diffusion2d import SolveDiffusion2D


def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """ 
    # Fixture
    w=60. 
    h=30.
    dx=0.2
    dy=0.15

    # Expected result
    nx= 300
    ny= 200

    # Actual result
    solver = SolveDiffusion2D()
    solver.initialize_domain(w, h, dx, dy)
    actual_nx = solver.nx
    actual_ny = solver.ny

    # Test
    assert actual_nx == nx
    assert actual_ny == ny

def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    # Fixture
    d=3.5
    T_cold=200.
    T_hot=600.

    # Expected result
    dt= 0.00113
    

    # Actual result
    solver = SolveDiffusion2D()
    solver.dx = 0.1
    solver.dy = 0.2
    solver.initialize_physical_parameters(d, T_cold, T_hot)
    actual_dt = pytest.approx(solver.dt, abs=0.0001)
  
    # Test
    assert actual_dt == dt
    


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    # Fixture

    # Expected result
    u= [[300., 300., 300., 300.],[300., 300., 300., 300.],[300., 300., 300., 300.],[300., 300., 300., 300.]]
    

    # Actual result
    solver = SolveDiffusion2D()
    solver.nx=4
    solver.ny=4
    solver.dx=0.1
    solver.dy=0.5
    solver.T_cold=330.
    solver.T_hot=930.
    actual_u = solver.set_initial_condition()
    
  
    # Test
    for index1,i in enumerate(u):
        for index2,j in enumerate(i):
            assert actual_u[index1][index2] == u[index1][index2]

    
