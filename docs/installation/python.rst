2.1 Python users
================

.. _python-installation:

Python 3.11-3.14 is supported. Using a virtual environment is recommended to isolate dependencies.

Install ``VOFTools`` from ``PyPI`` using:

.. code:: bash

   python -m pip install voftools

When a compatible precompiled package (wheel) is available for the Python version, operating system, and processor architecture, pip installs it without requiring C or Fortran compilers. Otherwise, pip attempts to build the package from the source distribution. Building from source requires ``GCC`` and ``GFortran``, together with the corresponding system development tools. Python build dependencies are installed automatically in an isolated build environment.

``NumPy`` is a required dependency and is installed automatically by pip. To run examples that use ``PyVista`` for visualization, also install:

.. code:: bash

   python -m pip install pyvista

To check that the library can be imported and query its default array dimensions, run:

.. code:: bash

   python -c "import voftools as v; print(v.voftools_dim3d())"  

For the default configuration, the expected output is ‘(140, 200)’.

2.1.1 Modifying the default values of :math:`\texttt{ns}` and :math:`\texttt{nv}`
---------------------------------------------------------------------------------

The parameters ‘``ns``’ and ‘``nv``’ are fixed when the library is compiled. Changing them therefore requires rebuilding the Python extension from source.

Download and extract the source package, then open a terminal in the extracted directory containing ‘``pyproject.toml``’. ``GCC`` and ``GFortran`` must be installed and available to the build system. Python build dependencies are installed automatically in an isolated environment.

Edit ‘``src/dimpol.h``’ to set the required dimensions. For example:

.. code:: fortran

   INTEGER, PARAMETER :: NS=240,NV=300

Alternatively, on systems with GNU Make and a compatible shell, the same file can be generated using:

.. code:: bash

   make dim NS=240 NV=300

This command updates the dimension definitions; it does not build or install the Python extension.

With the intended Python environment active and ``NumPy`` already installed as described in Section \ :ref:`2.1 <python-installation>`\ , rebuild and reinstall ``VOFTools`` from the source directory:

.. code:: bash

   python -m pip install --force-reinstall --no-deps --no-cache-dir .

The ``--no-deps`` option preserves the runtime dependencies already installed in the environment. Build dependencies are still managed automatically.

Verify the dimensions in a new Python process:

.. code:: bash

   python -c "import voftools as v; print(v.voftools_dim3d())"  

For the values used above, the expected output is ‘(240, 300)’. Restart any Python sessions or notebook kernels that had already imported ``VOFTools`` before using the rebuilt library.

2.1.2 Executing the test programs
---------------------------------

The Python examples are provided in the ‘``examples/python/``’ directory of the source package. Installing ``VOFTools`` with pip does not place these scripts in the current working directory.

To run the examples, extract the source package and open a terminal in its root directory. Activate the Python environment in which ``VOFTools`` is installed. Before running ‘``testfit.py``’, copy ‘``data/polygons-set.txt``’ to this working directory.

Run the examples using:

.. code:: bash

   python examples/python/test2d.py
   python examples/python/test3d.py
   python examples/python/testfit.py
   python examples/python/testparab.py

Input parameters for the Python examples are defined directly in the corresponding scripts. The ‘``vofvardef``’ configuration file is used by the C and Fortran examples ‘``test2d``’ and ‘``test3d``’.

Output files are written to the current working directory. The operations and expected results are described in Chapter \ :ref:`4 <sec:test-program>`\ .

The ‘``test3d.py``’ example uses ``PyVista`` to display the original and truncated cells. Close each visualization window to allow execution to continue. In environments without a compatible graphical display, the two ‘``grid.plot(...)``’ calls can be commented out to run the numerical calculations without opening windows. ``PyVista`` is still required by the remaining visualization-related code.
