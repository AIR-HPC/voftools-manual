4.2 PPIC operations
===================

.. _sec:ppic-operations:

The PPIC testing suite is divided into two primary components:

#. **Surface fitting:** Programs designed to obtain a paraboloid that volumetrically best fits a set of input polygons. This includes ``testfit.f90``, ``testfit.c``, and ``testfit.py``.

#. **Volume truncation and shifting:** Programs designed to compute the volume of the polyhedral approximation resulting from the intersection between a paraboloid and an arbitrary polyhedral cell, and shift the paraboloid position to enforce discrete volume conservation. This includes ``testparab.f90``, ``testparab.c``, and ``test­parab.py``.

The configuration and execution of the test programs are described in Sections \ :ref:`4.2.1 <sec:config-test-progs2>`\  for the fitting operation, and in Section \ :ref:`4.2.2 <sec:config-test-progs3>`\  for the volume truncation and shifting operations. For a comprehensive assessment of the PPIC operations,

refer to Reference [\ :ref:`14 <bib-lopez26>`\ ].

4.2.1 Configuration and execution of the fitting operation
----------------------------------------------------------

.. _sec:config-test-progs2:

In this program, the user must specify the origin (``vp0(1)``, ``vp0(2)``, ``vp0(3)``) and the orthonormal basis matrix

.. math::

   \left(
   \begin{split}
   \texttt{vn0(1,1)}, \texttt{vn0(1,2)}, \texttt{vn0(1,3)} \\
   \texttt{vn0(2,1)}, \texttt{vn0(2,2)}, \texttt{vn0(2,3)} \\
   \texttt{vn0(3,1)}, \texttt{vn0(3,2)}, \texttt{vn0(3,3)}  
   \end{split}
   \right)

defining the local coordinate system.

Additionally, the input parameters include the total number of polygons (``npol``) utilized for the paraboloid fitting and the vertex coordinates (``xv(i,j)``, ``yv(i,j)``, and ``zv(i,j)``) corresponding to vertex ``j`` of polygon ``i``. All these geometric data must be expressed in the global Cartesian coordinate system and are provided in a text file named ``polygons-set.txt``, which is automatically read by the program at runtime.

The program outputs the coefficients :math:`\texttt{coef}=[c_1,c_2,c_3,c_4,c_5,c_6]` of the fitted pa­ra­bo­loid, defined by Eq. (\ :ref:`3.1 <eq:parab>`\ ) within the local reference system, along with the sum of squared volumetric residuals (``errfit``) evaluated using the fitted coefficients.

The input data also include the number of polygons ``npol``, the number of vertices ``niv(i)`` and unit normal components ``xn(i), yn(i), zn(i)`` of each polygon, and the coordinates ``xv(i,j), yv(i,j), zv(i,j)`` of vertex ``j`` of polygon ``i``. Coordinates and normal vectors are expressed in the global Cartesian system. These data, together with the local reference system, are read from ``polygons-set.txt`` in the current working directory.

Finally, a Gnuplot script (``fitted-paraboloid.gnuplot``) is generated to visualize the fitted paraboloid and the set of polygons within the local reference system.

Example.
^^^^^^^^

This example demonstrates the execution of the paraboloid fitting routine using a predefined set of polygons. The input data is provided in the file named ``polygons-set.txt``, located in the ``data`` directory. This file is copied to the working directory and processed by the program, yielding the following results:

=========================== ======================
**Paraboloid coefficients** 
--------------------------------------------------
``coef(1)``                 -0.0004938819558816568
``coef(2)``                 -0.010011282362152601
``coef(3)``                 0.04436260142637836
``coef(4)``                 1.453899072370075
``coef(5)``                 0.0031810769178630947
``coef(6)``                 1.449920493501572
**Fitting error**           
--------------------------------------------------
``errfit``                  8.2316009696390840e-15
=========================== ======================

The program also generates two additional output files:

- ``polygons-set-lrs.txt``: Contains the coordinates of all polygon vertices transformed into the local reference system.

- ``fitted-paraboloid.gnuplot``: A Gnuplot script for visualizing the fitted paraboloid and the input polygons in the local coordinate frame.

To visualize the results, execute Gnuplot in a terminal and load the script:

::

   $ gnuplot
   gnuplot> load 'fitted-paraboloid.gnuplot'

The resulting plot is shown in Fig. \ :ref:`4.27 <fitted-paraboloid>`\ .

.. _fitted-paraboloid:

.. figure:: /_images/fitted-paraboloid.png
   :alt: Example of the fitting operation performed by the test program testfit. The paraboloid (green surface) is fitted to a set of polygons (magenta lines) defined in a local coordinate system.
   :align: center

   **Figure 4.27.** Example of the fitting operation performed by the test program ``testfit``. The paraboloid (green surface) is fitted to a set of polygons (magenta lines) defined in a local coordinate system.

4.2.2 Configuration and execution of volume truncation and shifting operations
------------------------------------------------------------------------------

.. _sec:config-test-progs3:

In this test program, the user must specify the coefficients of the paraboloid, along with the orientation and origin of the local coordinate system. These parameters are stored in the array ``cparab`` (length 12), where:

- The first six elements (:math:`c_1`–:math:`c_6`) represent the coefficients of the paraboloid equation within the **local** coordinate system.

- Elements 7-9 specify the components of the unit vector along the local ``f``-axis, expressed in the global coordinate system. Elements 10-12 specify the global coordinates of the local origin.

Additionally, the program requires the definition of the polyhedron (in the global coordinate system) used for volume computation and shifting operations. This geometry can be defined in two ways:

#. By passing the scalar value ``icelltype`` to the routine ``defpol3d`` (see Table \ :ref:`3.4 <geometries-index>`\  for predefined cell types).

#. By manually constructing the polyhedron vertices and faces.

.. _example.-1:

Example.
^^^^^^^^

This example demonstrates the volume truncation and shifting operations for a paraboloid defined in a local coordinate system. The paraboloid equation is given by:

.. math:: \texttt{f}(\texttt{u},\texttt{v}) = 4 \texttt{u}^2 + 4 \texttt{v}^2,

where :math:`(u, v)` are the local coordinates. The input array ``cparab`` (length 12) is configured as follows:

============== ===
``cparab(1)``  0.0
``cparab(2)``  0.0
``cparab(3)``  0.0
``cparab(4)``  4.0
``cparab(5)``  0.0
``cparab(6)``  4.0
``cparab(7)``  0.0
``cparab(8)``  0.0
``cparab(9)``  1.0
``cparab(10)`` 0.5
``cparab(11)`` 0.5
``cparab(12)`` 0.5
============== ===

Here, the first six elements correspond to the coefficients of the paraboloid (:math:`c_4=4, c_6=4`, others zero), and the last six elements define the local coordinate system origin :math:`(0.5, 0.5, 0.5)` and orientation vector :math:`(0, 0, 1)` in the global Cartesian frame.

The test case utilizes a cubic cell defined by ``icelltype = 11`` via the ``defpol3d`` routine. The simulation parameters are:

- Refinement parameter: :math:`\texttt{nc} = 4`.

- Target fluid volume fraction: :math:`0.5`, corresponding to a target volume of :math:`\texttt{vf} = 0.5\texttt{vt}`.

The program computes the volume of the polyhedral approximation of the region of intersection between the paraboloid and the cubic cell. It then shifts the paraboloid to enforce discrete volume conservation. The output includes:

#. The computed volume corresponding to the initial paraboloid (:math:`\sim 0.08216`).

#. The shifted coefficients of the paraboloid, exported to a text file named ``cparab.dat``. Note that only one coefficient, :math:`c_1`, is modified to satisfy the volume constraint, resulting in a new value of :math:`c_1 \approx -0.66263`.

#. The geometry of the polyhedron transformed into the local coordinate system, exported to a VTK file named ``pol00000.vtk``.

The Python script ``cellparabout.py``, located in the ``src`` directory, facilitates the visualization of the results. The visualization script requires ``NumPy`` and ``PyVista``. Copy ``cellparabout.py`` from the ``src`` directory to the working directory containing the files ``cparab.dat`` and ``pol00000.vtk``, and execute:

.. code:: python

   python cellparabout.py  

The script generates a PDF file named ``cellparabout.pdf`` (see Fig. \ :ref:`4.28 <cellparab>`\ (b); Fig. \ :ref:`4.28 <cellparab>`\ (a) corresponds to the equivalent result for the initial paraboloid).

.. _cellparab:

.. figure:: /_images/cellparab.png
   :alt: Example of the shifting operation performed by the test program testparab. (a) Before shifting: Initial paraboloid (transparent green surface) and cubic cell (transparent gray surfaces) in the local coordinate system (\texttt{u},\texttt{v},\texttt{f}). (b) After shifting: Equivalent result for the shifted paraboloid. The intersection between the paraboloid and the cubic cell boundaries is represented by red lines.
   :align: center

   **Figure 4.28.** Example of the shifting operation performed by the test program ``testparab``. (a) Before shifting: Initial paraboloid (transparent green surface) and cubic cell (transparent gray surfaces) in the local coordinate system :math:`(\texttt{u},\texttt{v},\texttt{f})`. (b) After shifting: Equivalent result for the shifted paraboloid. The intersection between the paraboloid and the cubic cell boundaries is represented by red lines.

Furthermore, Fig. \ :ref:`4.29 <cellparab-vf>`\  presents analogous results for tetrahedral and stellated cubic cells at fluid volume fractions :math:`\texttt{v}/\texttt{vt} = 0.05`, 0.25, 0.5, 0.75, and 0.95, illustrating the application of the shifting procedure to both convex and non-convex geometries.

.. _cellparab-vf:

.. figure:: /_images/cellparab-vf.png
   :alt: Equivalent to Fig. 4.28(b) but for (a) tetrahedral (\texttt{icelltype}=13) and (b) stellated cubic (\texttt{icelltype}=113) cells, and different fluid volume fractions \texttt{v}/\texttt{vt}.
   :align: center

   **Figure 4.29.** Equivalent to Fig. \ :ref:`4.28 <cellparab>`\ (b) but for (a) tetrahedral (:math:`\texttt{icelltype}=13`) and (b) stellated cubic (:math:`\texttt{icelltype}=113`) cells, and different fluid volume fractions :math:`\texttt{v}/\texttt{vt}`.

Test coverage.
^^^^^^^^^^^^^^

The test programs presented in this chapter exercise selected routines of the ``VOFTools`` library and illustrate representative applications. They do not constitute an exhaustive test suite covering every routine, input configuration, or geometric degeneracy. When applying the library to other configurations, users should follow the requirements documented for each routine and verify the results against suitable reference cases.
