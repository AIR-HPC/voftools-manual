2.2 C and Fortran users
=======================

.. _sec:cf-installation:

The source package includes a ``Makefile`` for building the static library and the C and Fortran examples. It uses ``GCC`` and ``GFortran`` by default and requires GNU Make and a compatible shell. On Windows, an appropriate build environment must be configured; compiler names, paths, and options may need to be adapted.

#. **Extract the source package in the chosen working directory**:

   .. code:: bash

      tar -zxvf voftools-6.tgz

#. **Enter the extracted directory**:

   .. code:: bash

      cd voftools-6

#. **Build the library and example programs**:

   .. code:: bash

      make

   The compiler commands can be specified explicitly. For example:

   .. code:: bash

      make CC=gcc F77=gfortran

   Replace ``gcc`` and ``gfortran`` with the appropriate executable names or paths if necessary. Compiler-specific options in the ``Makefile`` must also be reviewed when using a different compiler family.

   To use dimensions other than the defaults, specify both parameters:

   .. code:: bash

      make NS=240 NV=300

   This sets ``ns`` to 240 and ``nv`` to 300 in ``src/dimpol.h`` before compilation. When invoking ``make`` without these assignments, the ``Makefile`` uses its default values of 140 and 200.

   The build creates the static library ``lib/libvoftools.a`` and the following executables in the package root directory:

   - **C**: ``test2d_c``, ``test3d_c``, ``testfit_c``, and ``testparab_c``.

   - **Fortran**: ``test2d_f``, ``test3d_f``, ``testfit_f``, and ``testparab_f``.

   To clean the compiled files before rebuilding, run:

   .. code:: bash

      make clean

   Then repeat the build command, including any custom compiler settings and dimension values.

#. **Configure input parameters**: Before running ``test2d_c``, ``test2d_f``, ``test3d_c``, or ``test3d_f``, edit the ``vofvardef`` file in the working directory to select the desired case. The 2D and 3D programs read the same file, so its values must be adjusted when switching between cases. Parameter descriptions are provided in the example source files and in Chapter \ :ref:`4 <sec:test-program>`\ .

   The ``testfit`` and ``testparab`` programs do not use ``vofvardef``; their configuration is described in Section \ :ref:`4.2 <sec:ppic-operations>`\ .

   **Example configuration:** The following configuration corresponds to a 3D test case involving:

   - A half-space defined by the unit normal vector (:math:`\texttt{xnc}=0`; :math:`\texttt{ync}=-1`; :math:`\texttt{znc}=0`).

   - Intersection with a cubic cell (:math:`\texttt{icelltype}=11`) having a truncated volume fraction :math:`\texttt{f}=0.5`.

   - Computation of the distance from point :math:`P` (:math:`\texttt{xp}=0`; :math:`\texttt{yp}=0`; :math:`\texttt{zp}=0`) to the reconstructed PLIC interface. This distance calculation requires a convex interfacial polygon. The example program performs it only for the selected convex cell types and when the cutting plane leaves nonzero portions of the cell on both sides.

   - Estimation of the volume of a spherical material body (:math:`\texttt{ishape}=11`) within the cell using the initialization procedure with ``nc``\ =10 subdivisions per coordinate direction and tolerance ``tol``\ =10.

   .. code:: bash

      Cell geometry, ICELLTYPE:
      11
      Material body shape, ISHAPE:
      11
      Material volume/area fraction, F:
      0.5
      X coordinate of the unit-length normal vector of the interface plane, XNC:
      0.0
      Y coordinate of the unit-length normal vector of the interface plane, YNC:
      -1.0
      Z coordinate of the unit-length normal vector of the interface plane, ZNC:
      0.0            !Ignore for 2D test programs
      X coordinate of point P from which the distance is calculated, XP:
      0.0
      Y coordinate of point P from which the distance is calculated, YP:
      0.0
      Z coordinate of point P from which the distance is calculated, ZP:
      0.0            !Ignore for 2D test programs
      Subdivision number in the volume fraction cell initialization, NC:
      10
      Tolerance for the initialization procedure, TOL:
      10.0

#. **Execute a test program**: Run the executable from the package root directory, where the required input files are located. For example, to run the 3D Fortran test:

   .. code:: bash

      ./test3d_f

   To run the corresponding C test:

   .. code:: bash

      ./test3d_c

   The ``testfit`` executables require ``polygons-set.txt`` in the working directory; the ``Makefile`` copies this file from ``data/`` during the build. Output files are written to the working directory. See Chapter \ :ref:`4 <sec:test-program>`\  for the configuration and interpretation of each example.
