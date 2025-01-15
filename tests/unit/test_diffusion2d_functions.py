#import pytest
import numpy as np
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from diffusion2d import SolveDiffusion2D
from unittest import TestCase
"""
Tests for functions in class SolveDiffusion2D
"""

class TestDiffusion2D(TestCase):

    def setUp(self):
        self.solver = SolveDiffusion2D()
        self.tolerance=0.0001
        return super().setUp()
    
    def test_initialize_domain(self):
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
        self.solver.initialize_domain(w, h, dx, dy)
        actual_nx = self.solver.nx
        actual_ny = self.solver.ny

        # Test
        self.assertEqual(actual_nx, nx)
        self.assertEqual(actual_ny, ny)
        #assert actual_nx == nx
        #assert actual_ny == ny

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        # Fixture
        d=3.5
        T_cold=200.
        T_hot=600.

        # Expected result
        dt= 0.00113

        # Actual result
        self.solver.dx = 0.1
        self.solver.dy = 0.2
        self.solver.initialize_physical_parameters(d, T_cold, T_hot)
        actual_dt = self.solver.dt
        #actual_dt = pytest.approx(self.solver.dt, self.tolerance)
    
        # Test
        self.assertAlmostEqual(actual_dt, dt , 4)
        #assert actual_dt == dt

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        # Fixture

        # Expected result
        u= np.array([[300., 300., 300., 300.],
                     [300., 300., 300., 300.],
                     [300., 300., 300., 300.],
                     [300., 300., 300., 300.],
                     [300., 300., 300., 300.]])


        # Actual result
        self.solver.nx=5
        self.solver.ny=4
        self.solver.dx=0.5
        self.solver.dy=0.5
        self.solver.T_cold=300.
        self.solver.T_hot=900.
        actual_u = self.solver.set_initial_condition()

    
        # Test
        self.assertEqual(actual_u.shape, u.shape)
        #assert actual_u.shape == u.shape
        
        self.assertTrue(np.allclose(actual_u, u))
        #assert np.allclose(actual_u, u, self.tolerance)


