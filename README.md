# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)


### pytest log
#### test_initialize_domain
```powershell
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
```
#### test_initialize_physical_parameters
```powershell
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
```
#### test_set_initial_condition
```powershell
==================================================================================================== test session starts ====================================================================================================
platform win32 -- Python 3.12.8, pytest-8.3.4, pluggy-1.5.0
rootdir: C:\Users\johzi\OneDrive\Desktop\Master\Simulation\Exercise\Ex6\testing-python-exercise-wt2425
collected 5 items                                                                                                                                                                                                            

tests\integration\test_diffusion2d.py ..                                                                                                                                                                               [ 40%] 
tests\unit\test_diffusion2d_functions.py ..F                                                                                                                                                                           [100%]

========================================================================================================= FAILURES ========================================================================================================== 
________________________________________________________________________________________________ test_set_initial_condition _________________________________________________________________________________________________ 

    def test_set_initial_condition():
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
        solver = SolveDiffusion2D()
        solver.nx=5
        solver.ny=4
        solver.dx=0.5
        solver.dy=0.5
        solver.T_cold=300.
        solver.T_hot=900.
        actual_u = solver.set_initial_condition()


        # Test
        assert actual_u.shape == u.shape
>       assert np.allclose(actual_u, u, atol=50)
E       assert False
E        +  where False = <function allclose at 0x00000254BF0838B0>(array([[900., 900., 900., 900.],\n       [900., 900., 900., 900.],\n       [900., 900., 900., 900.],\n       [900., 900., 900., 900.],\n       [900., 900., 900., 900.]]), array([[300., 300., 300., 300.],\n       [300., 300., 300., 300.],\n       [300., 300., 300., 300.],\n       [300., 300., 300., 300.],\n       [300., 300., 300., 300.]]), atol=50)
E        +    where <function allclose at 0x00000254BF0838B0> = np.allclose

tests\unit\test_diffusion2d_functions.py:87: AssertionError
================================================================================================== short test summary info ================================================================================================== 
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert False
================================================================================================ 1 failed, 4 passed in 0.67s ================================================================================================
```
### unittest log

#### test_initialize_domain
```powershell
Fdt = 0.0011428571428571432
..
======================================================================
FAIL: test_initialize_domain (test_diffusion2d_functions.TestDiffusion2D.test_initialize_domain)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\johzi\OneDrive\Desktop\Master\Simulation\Exercise\Ex6\testing-python-exercise-wt2425\tests\unit\test_diffusion2d_functions.py", line 43, in test_initialize_domain
    self.assertEqual(actual_ny, ny)
AssertionError: 4 != 200

----------------------------------------------------------------------
Ran 3 tests in 0.002s

FAILED (failures=1)
```
#### test_initialize_physical_parameters
```powershell
.dt = 0.0019047619047619052
F.
======================================================================
FAIL: test_initialize_physical_parameters (test_diffusion2d_functions.TestDiffusion2D.test_initialize_physical_parameters)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\johzi\OneDrive\Desktop\Master\Simulation\Exercise\Ex6\testing-python-exercise-wt2425\tests\unit\test_diffusion2d_functions.py", line 67, in test_initialize_physical_parameters
    self.assertAlmostEqual(actual_dt, dt , 4)
AssertionError: 0.0019047619047619052 != 0.00113 within 4 places (0.0007747619047619053 difference)

----------------------------------------------------------------------
Ran 3 tests in 0.002s

FAILED (failures=1)
```
#### test_set_initial_condition
```powershell
.dt = 0.0011428571428571432
.F
======================================================================
FAIL: test_set_initial_condition (test_diffusion2d_functions.TestDiffusion2D.test_set_initial_condition)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\johzi\OneDrive\Desktop\Master\Simulation\Exercise\Ex6\testing-python-exercise-wt2425\tests\unit\test_diffusion2d_functions.py", line 96, in test_set_initial_condition
    self.assertTrue(np.allclose(actual_u, u))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.002s

FAILED (failures=1)
```
## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
