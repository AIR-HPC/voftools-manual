1 Introduction
==============

``VOFTools`` is a software package designed to provide analytical and geometrical tools for 2D/3D volume-of-fluid (VOF) methods in arbitrary grids. It supports both convex or non-convex cell types, which are common in complex computational domains. The library includes efficient algorithms for area/volume computation, truncation operations frequently encountered in VOF methods, and area/volume conservation enforcement (VCE) to accurately locate interfaces in piecewise linear interface calculation (PLIC) and piecewise paraboloid interface calculation (PPIC) reconstructions. Additionally, ``VOFTools`` supports liquid area/volume fraction initialization and computes the shortest distance from a given point to the reconstructed PLIC interface. Previous versions of this library have been described in [\ :ref:`6 <bib-lopez08>`\ , \ :ref:`7 <bib-lopez13>`\ , \ :ref:`8 <bib-lopez16>`\ , \ :ref:`9 <bib-lopez17>`\ , \ :ref:`11 <bib-lopez19>`\ , \ :ref:`12 <bib-lopez18cpc>`\ ].

The current version has been extensively revised and restructured to enhance interoperability through the ``ISO_C_BINDING`` module. This new version incorporates several improvements in both accuracy and computational efficiency for handling intersections between polyhedra and half-spaces, as well as optimized methods for computing the interface position to cut off a given area or volume fraction from an arbitrary polygonal/polyhedral grid cell during PLIC reconstruction. Furthermore, the updated codebase includes new routines designed specifically for:

#. Paraboloid reconstruction via volumetric-error-minimization fitting of discrete polygonal data.

#. Computation of the intersection volume between the PPIC fluid domain and an arbitrary polyhedral cell.

#. Conservative PPIC reconstruction for interface localization in arbitrary polyhedral cells.

#. Efficient computation of the average position of clipped vertices and the resulting volume arising from the intersection of an arbitrary polyhedron with a half-space. This routine is particularly advantageous for PLIC reconstruction algorithms and unsplit advection schemes based on fluid-volume intersection advection (FVIA).

#. Three-dimensional clipping of an arbitrary oriented planar polygon by a half-space, including the computation of the resulting area. This feature is essential for unsplit advection schemes based on wetted-area time-integration advection (WATIA).

#. Auxiliary computational utilities for robust simulation setup, including geometric bounding-box estimation and dynamic memory configuration.

These enhancements significantly improve the code’s overall functionality, robustness, and computational efficiency in handling complex geometric calculations critical to advanced VOF methods. Comprehensive implementation details and performance analyses are provided in [\ :ref:`15 <bib-lopez21>`\ , \ :ref:`13 <bib-lopez24>`\ , \ :ref:`14 <bib-lopez26>`\ ].

``VOFTools`` is implemented in Fortran, with C and Python (v3) interfaces provided to facilitate interoperability. The Python bindings utilize the ``f2py`` module from the ``NumPy`` library [\ :ref:`19 <bib-f2py>`\ ]. To promote reproducibility and ease of access, ``VOFTools`` is distributed via the Python Package Index (PyPI) [\ :ref:`18 <bib-pypi>`\ ].

The package includes the following key components:

- ``src``: Directory containing the core source code and interface definitions.

  - ``dimpol.h``: Header file declaring parameters ``ns`` and ``nv`` used for pre-allocating arrays in polytope computations.

  - ``voftools.f90``: Fortran source code implementing the core routines of the ``VOFTools`` library.

  - ``uservoftools.f90``: Fortran source file containing user-defined routines and functions, allowing for custom logic integration.

  - ``cvoftools.h``: C header file declaring the interfaces for the core ``VOFTools`` library routines, enabling use in C programs.

  - ``cuservoftools.h``: C header file exposing the user-defined routines from ``uservoftools.f90`` for integration into C applications.

  - ``voftools.pyf``: F2PY signature file that defines how Fortran routines in ``voftools.f90`` are exposed to Python, facilitating binary interface compatibility.

  - ``cellparabout.py``: Python script that reads a polyhedron from a VTK file and a set of paraboloid coefficients from a text file. It then generates the corresponding paraboloid surface, computes the intersection curve between the polyhedron and the paraboloid, and visualizes the results using ``pyvista``.

- ``__init__.py``: Python package initialization file, enabling the directory to be imported as a module.

- ``.f2py_f2cmap``: Configuration file for ``NumPy``\ ’s ``f2py`` tool, mapping Fortran data types to corresponding C types to ensure correct memory layout and data transfer.

- ``examples``: Directory containing test programs demonstrating library usage in Python, C, and Fortran. Each language example directory includes:

  - ``test2d``: Script for 2D PLIC operations.

  - ``test3d``: Script for 3D PLIC operations.

  - ``testfit``: Script for PPIC fitting operation.

  - ``testparab``: Script for PPIC truncation and shifting operations.

- ``data``: Directory containing static input data files (e.g., polygon sets) required by the test programs.

- ``vofvardef``: Input configuration file providing parameters for the C and Fortran test executables.

- ``Makefile``: Build script that automates the compilation of the ``VOFTools`` library and the execution of C/Fortran test programs.

- ``meson.build``: Meson build system configuration file defining dependencies, compiler flags, and installation rules for the ``VOFTools`` library.

- ``pyproject.toml``: Python packaging configuration that specifies metadata, dependencies, and build settings, supporting Python versions 3.11-3.14 across Linux, macOS, and Windows.

- ``doc``: Directory containing the user manual in ``PDF`` format.

  - ``user-manual-voftools-6.pdf``.

- ``readme.md``: Project overview file.

- ``LICENSE``: Copy of the GNU General Public License (GPL), Version 3.

Note:
^^^^^

The index notation used in the illustrative examples throughout this manual follows the convention of starting from 1, which is consistent with Fortran array indexing. In contrast, C and Python use zero-based indexing. Users should be aware of this distinction when interpreting array indices in the provided examples.
