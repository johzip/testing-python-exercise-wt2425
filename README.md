# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)


### pytest log
#### test_initialize_domain
==================================== test session starts =====================================
platform win32 -- Python 3.12.8, pytest-8.3.4, pluggy-1.5.0
rootdir: C:\Users\johzi\OneDrive\Desktop\Master\Simulation\Exercise\Ex6\testing-python-exercise-wt2425
collected 5 items                                                                             

tests\integration\test_diffusion2d.py ..                                                [ 40%] 
tests\unit\test_diffusion2d_functions.py F..                                            [100%]

========================================== FAILURES ========================================== 
___________________________________ test_initialize_domain ___________________________________ 

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
>       assert actual_nx == nx
E       assert 150 == 300

tests\unit\test_diffusion2d_functions.py:30: AssertionError
================================== short test summary info =================================== 
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 150 == 300    
================================ 1 failed, 4 passed in 0.54s =================================

#### test_initialize_physical_parameters
=============================================== test session starts ================================================
platform win32 -- Python 3.12.8, pytest-8.3.4, pluggy-1.5.0
rootdir: C:\Users\johzi\OneDrive\Desktop\Master\Simulation\Exercise\Ex6\testing-python-exercise-wt2425
collected 5 items                                                                                                   

tests\integration\test_diffusion2d.py ..                                                                      [ 40%] 
tests\unit\test_diffusion2d_functions.py .F.                                                                  [100%]

===================================================== FAILURES ===================================================== 
_______________________________________ test_initialize_physical_parameters ________________________________________ 

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
>       assert actual_dt == dt
E       assert 0.004571428571428573 ± 1.0e-04 == 0.00113
E
E         comparison failed
E         Obtained: 0.00113
E         Expected: 0.004571428571428573 ± 1.0e-04

tests\unit\test_diffusion2d_functions.py:55: AssertionError
----------------------------------------------- Captured stdout call ----------------------------------------------- 
dt = 0.004571428571428573
============================================= short test summary info ============================================== 
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.004571428571428573 ± 1.0e-04 == 0.00113
=========================================== 1 failed, 4 passed in 0.50s ============================================

### unittest log

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
