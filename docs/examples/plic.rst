4.1 PLIC operations
===================

.. _sec:plic-operations:

Test programs for both 2D and 3D PLIC operations are implemented in Fortran (``test2d.f90``, ``test3d.f90``), C (``test2d.c``, ``test3d.c``), and Python (``test2d.py``, ``test3d.py``).

The configuration and execution of these test programs are detailed in Section \ :ref:`4.1.1 <sec:config-test-progs>`\ . Subsequently, a runtime flow analysis along with quantitative accuracy results obtained from the tests are presented in Section \ :ref:`4.1.2 <sec:assessment>`\ .

4.1.1 Configuration and execution of test programs
--------------------------------------------------

.. _sec:config-test-progs:

The test programs require specific input data to define each test case. These inputs are categorized as follows:

- **Cell geometry:** The topological and geometric definition of the computational cell (vertices, connectivity, and face normals, for 3D cells).

- **Initial material distribution:** The material body geometry specified through an implicit function

  defining the initial material body, whose volume fraction within the cell is computed by the initialization procedure (``initf2d``/``initf3d``).

- **Target area/volume fraction:** The prescribed liquid fraction ``f``. The target liquid area or volume supplied to the VCE solver is calculated as :math:`\texttt{v} = \texttt{f} \texttt{vt}`, where ``vt`` is the total cell area or volume.

- **Interface normal vector:** The unit normal vector :math:`\boldsymbol{n}` to the reconstructed PLIC interface within the cell.

- **Distance evaluation point:** The coordinates of the point from which the Euclidean distance to the reconstructed PLIC interface is calculated (used in routines such as ``dist2d``/``dist3d``).

- **Numerical parameters:** The Cartesian shadow-grid resolution ``nc`` and the threshold parameter ``tol`` used in the preliminary vertex-based classification of the initialization procedure.

For the Fortran and C test programs, input data are provided via the file ``vofvardef``, included in the package distribution. Detailed information regarding this file is available in Chapter \ :ref:`2 <installation>`\ . These inputs are read by invoking the routine ``vofvardef`` located in ``uservoftools.f90``. This routine can be invoked as follows:

**Fortran:**

.. code:: fortran

   call vofvardef(f,icelltype,ishape,nc,tol,xnc,xp,ync,yp,znc, &
                  zp)

**C:**

.. code:: c

   vofvardef(&f,&icelltype,&ishape,&nc,&tol,&xnc,&xp,&ync,&yp,&znc,
           &zp);

**Arguments:**

+-------------------+---------+---------+-------------------------------------------------------------------------------------------------------------+
| ``f``             | ``OUT`` | ``W_P`` | target volume/area fraction                                                                                 |
+-------------------+---------+---------+-------------------------------------------------------------------------------------------------------------+
| ``icelltype``     | ``OUT`` | ``I_P`` | cell geometry index (see Table \ :ref:`3.4 <geometries-index>`\ )                                           |
+-------------------+---------+---------+-------------------------------------------------------------------------------------------------------------+
| ``ishape``        | ``OUT`` | ``I_P`` | material body shape index (see Table \ :ref:`4.1 <body-shape-index>`\ )                                     |
+-------------------+---------+---------+-------------------------------------------------------------------------------------------------------------+
| ``nc``            | ``OUT`` | ``I_P`` | sub-grid resolution along each axis                                                                         |
+-------------------+---------+---------+-------------------------------------------------------------------------------------------------------------+
| ``tol``           | ``OUT`` | ``W_P`` | positive threshold parameter used in the preliminary vertex-based classification of ``initf2d``/``initf3d`` |
+-------------------+---------+---------+-------------------------------------------------------------------------------------------------------------+
| ``xnc, ync, znc`` | ``OUT`` | ``W_P`` | normal vector components :math:`\boldsymbol{n}`                                                             |
+-------------------+---------+---------+-------------------------------------------------------------------------------------------------------------+
| ``xp, yp, zp``    | ``OUT`` | ``W_P`` | Point :math:`P` coordinates for distance calculation                                                        |
+-------------------+---------+---------+-------------------------------------------------------------------------------------------------------------+

**Note:** The indices for ``icelltype`` and ``ishape`` are defined in Tables \ :ref:`3.4 <geometries-index>`\  and \ :ref:`4.1 <body-shape-index>`\ , respectively. The implicit functions corresponding to each shape are defined in the file ``uservoftools.f90``. The ``vofvardef`` input file must be available in the current working directory when running the Fortran or C test programs.

For the Python test programs ``test2d.py`` and ``test3d.py``, input data are configured directly within the script files. This includes both the geometric parameters (cell geometry, target volume fraction, normal vector, etc.) and the user-defined implicit functions that define the material body shapes. This approach allows for immediate inspection and modification of test cases without relying on external configuration modules or compilation steps.

Algorithmic workflow
~~~~~~~~~~~~~~~~~~~~

The test programs execute a sequential workflow to validate each PLIC operation. The standard flow for both 2D and 3D cases is as follows:

.. _body-shape-index:

**Table 4.1.** Values of the ``ishape`` index used to denote the body shapes considered in the test programs.

+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ishape`` **index** | **Body shape**                                                                                                                                                                                                                                                                                                                                              |
+======================+=============================================================================================================================================================================================================================================================================================================================================================+
| *3D geometries*                                                                                                                                                                                                                                                                                                                                                                    |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                      |                                                                                                                                                                                                                                                                                                                                                             |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 11                   | Sphere with radius 0.325 defined by the implicit function :math:`\displaystyle f(x,y,z)=0.325^2-(x-0.5)^2-(y-0.5)^2-(z-0.5)^2`                                                                                                                                                                                                                              |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                      |                                                                                                                                                                                                                                                                                                                                                             |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 12                   | Torus with major radius :math:`2/3` and minor radius :math:`1/3` defined by the implicit function :math:`\displaystyle f(x,y,z)=\left(\frac{1}{3}\right)^2-\left\{\frac{2}{3}-\left[(x-0.5)^2+(z-0.5)^2\right]^{1/2}\right\}^2-(y-0.5)^2`                                                                                                                   |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                      |                                                                                                                                                                                                                                                                                                                                                             |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 13                   | Union between a sphere with radius 0.25 defined by the implicit function :math:`\displaystyle \phi_1(x,y,z)=0.25^2-(x-0.5)^2-(y-0.5)^2-(z-0.5)^2` and a paraboloid defined by the implicit function :math:`\displaystyle \phi_2(x,y,z)=z-4x^2-4y^2+4(x+y)-2.25`. The material region is defined by :math:`\phi(x,y,z)=\max(\phi_1(x,y,z),\phi_2(x,y,z))>0`. |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                      |                                                                                                                                                                                                                                                                                                                                                             |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *2D geometries*                                                                                                                                                                                                                                                                                                                                                                    |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                      |                                                                                                                                                                                                                                                                                                                                                             |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1                    | Circle with radius 0.325 defined by the implicit function :math:`\displaystyle f(x,y)=0.325^2-(x-0.5)^2-(y-0.5)^2`                                                                                                                                                                                                                                          |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                      |                                                                                                                                                                                                                                                                                                                                                             |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2                    | Ellipse with semi-major axis :math:`0.5` and semi-minor axis :math:`0.2` defined by the implicit function :math:`\displaystyle f(x,y)=1-\left(\frac{x-0.5}{0.5}\right)^2-\left(\frac{y-0.5}{0.2}\right)^2`                                                                                                                                                  |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                      |                                                                                                                                                                                                                                                                                                                                                             |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. **Cell Volume/Area Computation:** The total area/volume (``vt``) of the computational cell is computed using ``toolv3d`` (3D) or ``toolv2d`` (2D). This value serves as the normalization reference for subsequent fraction calculations.

#. **Interface reconstruction (area/volume conservation enforcement):** A planar interface with a prescribed normal vector :math:`\boldsymbol{n}` is positioned within the cell such that it cuts off a target liquid area/volume fraction ``f`` (the solver receives :math:`\texttt{v}=\texttt{f} \texttt{vt}`). The position of this interface, defined by the constant :math:`\texttt{c}` in the equation :math:`\boldsymbol{n} \cdot \boldsymbol{x} + \texttt{c} = 0`, is determined by solving the VCE problem using ``enforv3d`` (3D) or ``enforv2d`` (2D) (see Fig. \ :ref:`4.1 <hexahedron-test-pr1>`\ ).

   .. _hexahedron-test-pr1:

   .. figure:: /_images/hexahedron-test-pr1.png
      :alt: Positioning the interface by solving the VCE problem on a hexahedral cell.
      :align: center

      **Figure 4.1.** Positioning the interface by solving the VCE problem on a hexahedral cell.

#. **Polyhedral/polygon clipping:** A working copy of the original cell geometry is truncated by the reconstructed interface plane/line. This is achieved by computing the intersection between the original cell and the half-space :math:`\boldsymbol{n} \cdot \boldsymbol{x} + \texttt{c} > 0` using ``inte3d`` (3D) or ``inte2d`` (2D) (see Fig. \ :ref:`4.2 <hexahedron-test-pr2>`\ ).

   - The routines ``inte3d`` and ``inte2d`` update the working geometry in place when truncation occurs. If ``icontp = 0``, the retained region is empty and its volume or area must be set to zero explicitly, since the input geometry remains unchanged. Otherwise, its volume or area can be obtained using ``toolv3d`` or ``toolv2d``.

   - In 3D, when explicit truncated geometry is not required, ``intv3d`` can compute the retained volume directly from the original cell. The routine ``intc3d`` returns the arithmetic mean of the intersection-vertex coordinates (:math:`\times` symbols in the left picture of Fig. \ :ref:`4.2 <hexahedron-test-pr2>`\ ), rather than an area or volume centroid.

   .. _hexahedron-test-pr2:

   .. figure:: /_images/hexahedron-test-pr4.png
      :alt: Truncation of the hexahedral cell by a plane containing the PLIC interface (the intersection vertices are marked with an \times symbol in the left picture).
      :align: center

      **Figure 4.2.** Truncation of the hexahedral cell by a plane containing the PLIC interface (the intersection vertices are marked with an :math:`\times` symbol in the left picture).

#. **Distance calculation:**  [1]_ The Euclidean distance from a user-defined point :math:`P` to the newly formed interface edge (in 2D) or face (in 3D) is computed using ``dist2d`` or ``dist3d``, respectively, for convex cells (see Fig. \ :ref:`4.3 <hexahedron-test-pr3>`\ ).

   .. _hexahedron-test-pr3:

   .. figure:: /_images/hexahedron-test-pr3.png
      :alt: Computation of the distance from point P to the reconstructed PLIC interface.
      :align: center

      **Figure 4.3.** Computation of the distance from point :math:`P` to the reconstructed PLIC interface.

#. **Initialization via implicit function:** To validate the initialization routines for complex interfaces, the volume/area fraction of a material body defined by an implicit function :math:`\phi(x,y)` in 2D and :math:`\phi(x,y,z)` in 3D (defined in ``uservoftools.f90`` for the Fortran/C examples and directly in the scripts for the Python examples) is computed within the cell using ``initf3d`` (3D) or ``initf2d`` (2D) (Fig. \ :ref:`4.4 <test-program-initf>`\  shows a 3D example for a non-convex cell). This process involves superimposing a Cartesian shadow grid on the polyhedral/polygonal domain.

   .. _test-program-initf:

   .. figure:: /_images/test-program-initf.png
      :alt: Initialization of the volume of a spherical material body contained inside a non-convex cell (example corresponding to \texttt{icelltype}=113 and \texttt{ishape}=11).
      :align: center

      **Figure 4.4.** Initialization of the volume of a spherical material body contained inside a non-convex cell (example corresponding to :math:`\texttt{icelltype}=113` and :math:`\texttt{ishape}=11`).

In the following, several examples of the execution of the 2D and 3D test programs are presented.

Example 1.
^^^^^^^^^^

.. _tab:2dexample1:

**Table 4.2.** Input data for example 1.

============== =================
``icelltype``: 1
``ishape``:    1
``f``:         0.5
``xnc, ync``:  0.0, :math:`-1.0`
``xp, yp``:    0.0, 0.0
``nc``:        10
``tol``:       10.0
============== =================

Table \ :ref:`4.2 <tab:2dexample1>`\  summarizes the input parameters considered for this 2D example. The execution of the 2D test program (``test2d``\ :math:`\_`\ ``f``, ``test2d``\ :math:`\_`\ ``c``, or ``python test2d.py``) yields the following results:

+------------------------------------------------------------------------------------------------------+----------+
| Total cell area, ``vt``:                                                                             | 1.0      |
+------------------------------------------------------------------------------------------------------+----------+
| Solution of the VCE problem, ``c``:                                                                  | 0.5      |
+------------------------------------------------------------------------------------------------------+----------+
| Distance from :math:`\boldsymbol{x}_P=(\texttt{xp}, \texttt{yp})` to the interfacial segment, ``d``: | 0.5      |
+------------------------------------------------------------------------------------------------------+----------+
| Material area fraction in the cell, ``vf``:                                                          | 0.322155 |
+------------------------------------------------------------------------------------------------------+----------+

Fig. \ :ref:`4.5 <2dexample1>`\  illustrates the results provided by the test program.

.. _2dexample1:

.. figure:: /_images/2dexample1.png
   :alt: Illustration of the results produced by the 2D test program for the input data corresponding to those of Table 4.2.
   :align: center

   **Figure 4.5.** Illustration of the results produced by the 2D test program for the input data corresponding to those of Table \ :ref:`4.2 <tab:2dexample1>`\ .

By changing the position of point :math:`P` to :math:`(-1,0)`, :math:`(0.5,0)` and :math:`(2,0)` the test program produces, respectively, the results shown in Figs. \ :ref:`4.6 <2dexample1b>`\ (a), \ :ref:`4.6 <2dexample1b>`\ (b) and \ :ref:`4.6 <2dexample1b>`\ (c).

.. _2dexample1b:

.. figure:: /_images/2dexample1b.png
   :alt: Distance d produced by the test program for the input data corresponding to those of Table 4.2 but changing the position of the point P to (a) (-1,0), (b) (0.5,0) and (c) (2,0).
   :align: center

   **Figure 4.6.** Distance ``d`` produced by the test program for the input data corresponding to those of Table \ :ref:`4.2 <tab:2dexample1>`\  but changing the position of the point :math:`P` to (a) :math:`(-1,0)`, (b) :math:`(0.5,0)` and (c) :math:`(2,0)`.

Note that the exact area fraction of the circular material body contained in the cell is

.. math:: \texttt{vf}_\mathrm{exact}=\pi 0.325^2.

Thus, the initialization error obtained using a division number :math:`\texttt{nc}=10` is :math:`9.7\times 10^{-3}`. Increasing the division number to :math:`\texttt{nc}=20`, the material area fraction in the cell results as :math:`\texttt{vf}=0.329106` producing an initialization error equal to :math:`2.7\times 10^{-3}`. Using the absolute error :math:`E=|\texttt{vf}-\texttt{vf}_{\mathrm{exact}}|`, these two resolutions give an observed convergence order of approximately :math:`p=\log_2(E_{10}/E_{20})=1.83`, suggesting nearly second-order behavior for this example.

Example 2.
^^^^^^^^^^

.. _tab:2dexample2:

**Table 4.3.** Input data for example 2.

============== ======================================
``icelltype``: 106
``ishape``:    1
``f``:         0.5
``xnc, ync``:  :math:`1/\sqrt{2}`, :math:`1/\sqrt{2}`
``xp, yp``:    -
``nc``:        10
``tol``:       10.0
============== ======================================

This example demonstrates the PLIC reconstruction process for a non-convex polygonal cell. The distance calculation is omitted in this test because the reconstructed interface in a non-convex cell may consist of multiple segments, where­as ``dist2d`` computes the distance to a single segment.

Table \ :ref:`4.3 <tab:2dexample2>`\  shows the input data considered for this 2D example. The execution of the 2D test program (``test2d``\ :math:`\_`\ ``f``, ``test2d``\ :math:`\_`\ ``c`` or ``python test2d.py``) produces the following results:

=========================================== ===================
Area of the cell, ``vt``:                   0.79
Solution of the VCE problem, ``c``:         :math:`-1/\sqrt{2}`
Material area fraction in the cell, ``vf``: 0.148487
=========================================== ===================

Fig. \ :ref:`4.7 <2dexample2>`\  illustrates the results provided by the test program.

.. _2dexample2:

.. figure:: /_images/2dexample2.png
   :alt: Illustration of the results produced by the 2D test program for the input data corresponding to those of Table 4.3.
   :align: center

   **Figure 4.7.** Illustration of the results produced by the 2D test program for the input data corresponding to those of Table \ :ref:`4.3 <tab:2dexample2>`\ .

The exact area fraction of the circular material body contained in the cell is, for this example,

.. math:: \texttt{vf}_\mathrm{exact}=\frac{2\times 0.325^2 (\theta -\sin\theta)+\frac{1}{5^2}}{1-\frac{1}{2^2}+\frac{1}{5^2}},

where :math:`\theta=2\arccos\left[1/\left(2^2\times 0.325 \right) \right]`. Thus, the initialization error obtained using a division number :math:`\texttt{nc}=10` is :math:`1.0\times 10^{-2}`. Increasing the division number to :math:`\texttt{nc}=20`, the material area fraction in the cell results as :math:`\texttt{vf}=0.155460` producing an initialization error equal to :math:`3.0\times 10^{-3}`. Using the absolute error :math:`E=|\texttt{vf}-\texttt{vf}_{\mathrm{exact}}|`, these two resolutions give an observed convergence order of approximately :math:`p=\log_2(E_{10}/E_{20})=1.73`.

Example 3.
^^^^^^^^^^

.. _tab:3dexample1:

**Table 4.4.** Input data for example 3.

================== ================
``icelltype``:     11
``ishape``:        11
``f``:             0.5
``xnc, ync, znc``: 0, :math:`-1`, 0
``xp, yp, zp``:    0, 0, 0
``nc``:            10
``tol``:           10.0
================== ================

This example demonstrates the PLIC reconstruction process for a polyhedral cell. Table \ :ref:`4.4 <tab:3dexample1>`\  summarizes the input data considered for this 3D example. The execution of the test program (``test3d``\ :math:`\_`\ ``f``, ``test3d``\ :math:`\_`\ ``c``, or ``python test3d.py``) yields the following results:

+------------------------------------------------------------------------------------------------------------------------+---------------+
| Volume of the cell, ``vt``:                                                                                            | 1.0           |
+------------------------------------------------------------------------------------------------------------------------+---------------+
| Solution of the VCE problem, ``c``:                                                                                    | 0.5           |
+------------------------------------------------------------------------------------------------------------------------+---------------+
| Truncated volume (``inte3d``\ :math:`+`\ ``toolv3d``), ``vol``:                                                        | 0.5           |
+------------------------------------------------------------------------------------------------------------------------+---------------+
| Truncated volume (``intv3d``), ``vol``:                                                                                | 0.5           |
+------------------------------------------------------------------------------------------------------------------------+---------------+
| Geometric center :math:`\boldsymbol{x}_c=(\texttt{xc}, \texttt{yc}, \texttt{zc})` of the set of intersection vertices: | (0.5,0.5,0.5) |
+------------------------------------------------------------------------------------------------------------------------+---------------+
| Distance from :math:`\boldsymbol{x}_P=(\texttt{xp}, \texttt{yp}, \texttt{zp})` to the interfacial polygon, ``d``:      | 0.5           |
+------------------------------------------------------------------------------------------------------------------------+---------------+
| Material area fraction in the cell, ``vf``:                                                                            | 0.133985      |
+------------------------------------------------------------------------------------------------------------------------+---------------+

Fig. \ :ref:`4.8 <3dexample1>`\  illustrates the results provided by the test program.

.. _3dexample1:

.. figure:: /_images/3dexample1.png
   :alt: Illustration of the results produced by the 3D test program for the input data corresponding to those of Table 4.4.
   :align: center

   **Figure 4.8.** Illustration of the results produced by the 3D test program for the input data corresponding to those of Table \ :ref:`4.4 <tab:3dexample1>`\ .

By changing the position of point :math:`P` to :math:`(0.5,0,0.5)`, :math:`(-0.5,0,1.5)` and :math:`(1.5,0,0.5)` the test program produces, respectively, the results shown in Figs. \ :ref:`4.9 <3dexample1b>`\ (a), \ :ref:`4.9 <3dexample1b>`\ (b) and \ :ref:`4.9 <3dexample1b>`\ (c).

.. _3dexample1b:

.. figure:: /_images/3dexample1b.png
   :alt: Distance \texttt{d} produced by the test program for the input data corresponding to those of Table 4.4 but changing the position of the point P to (a) (0.5,0,0.5), (b) (-0.5,0,1.5) and (c) (1.5,0,0.5).
   :align: center

   **Figure 4.9.** Distance :math:`\texttt{d}` produced by the test program for the input data corresponding to those of Table \ :ref:`4.4 <tab:3dexample1>`\  but changing the position of the point :math:`P` to (a) :math:`(0.5,0,0.5)`, (b) :math:`(-0.5,0,1.5)` and (c) :math:`(1.5,0,0.5)`.

The exact volume fraction of the spherical material body contained in the cell is

.. math:: \texttt{vf}_\mathrm{exact}=\frac{4}{3}\pi 0.325^3.

The absolute initialization error is approximately :math:`9.8\times10^{-3}` for :math:`\texttt{nc} = 10`. Increasing the resolution to :math:`\texttt{nc} = 20` gives :math:`\texttt{vf}=0.141256`, with an absolute error of approximately :math:`2.5\times10^{-3}`. These two resolutions give an observed convergence order of approximately :math:`p=\log_2(E_{10}/E_{20})=1.95`, consistent with nearly second-order behavior for this example.

Example 4.
^^^^^^^^^^

.. _tab:3dexample2:

**Table 4.5.** Input data for example 4.

================== ================
``icelltype``:     113
``ishape``:        12
``f``:             0.5
``xnc, ync, znc``: 0, :math:`-1`, 0
``xp, yp, zp``:    -
``nc``:            10
``tol``:           10.0
================== ================

This example demonstrates the PLIC reconstruction process for a non-convex polyhedral cell. Table \ :ref:`4.5 <tab:3dexample2>`\  shows the input data considered for this 3D example. The execution of the 3D test program (``test3d``\ :math:`\_`\ ``f`` or ``test3d``\ :math:`\_`\ ``c``) produces the following results:

+------------------------------------------------------------------------------------------------------------------------+---------------+
| Volume of the cell, ``vt``:                                                                                            | 3.0           |
+------------------------------------------------------------------------------------------------------------------------+---------------+
| Solution of the VCE problem, ``c``:                                                                                    | 0.5           |
+------------------------------------------------------------------------------------------------------------------------+---------------+
| Truncated volume (``inte3d``\ :math:`+`\ ``toolv3d``), ``vol``:                                                        | 1.5           |
+------------------------------------------------------------------------------------------------------------------------+---------------+
| Truncated volume (``intv3d``), ``vol``:                                                                                | 1.5           |
+------------------------------------------------------------------------------------------------------------------------+---------------+
| Geometric center :math:`\boldsymbol{x}_c=(\texttt{xc}, \texttt{yc}, \texttt{zc})` of the set of intersection vertices: | (0.5,0.5,0.0) |
+------------------------------------------------------------------------------------------------------------------------+---------------+
| Material volume fraction in the cell, ``vf``:                                                                          | 0.321329      |
+------------------------------------------------------------------------------------------------------------------------+---------------+

Fig. \ :ref:`4.10 <3dexample2>`\  illustrates the geometric configuration and results provided by the test program.

.. _3dexample2:

.. figure:: /_images/3dexample2.png
   :alt: Illustration of the results produced by the test program for the input data corresponding to those of Table 4.5.
   :align: center

   **Figure 4.10.** Illustration of the results produced by the test program for the input data corresponding to those of Table \ :ref:`4.5 <tab:3dexample2>`\ .

A reference volume fraction is estimated using Richardson extrapolation from the solutions obtained with :math:`\texttt{nc} = 512` and :math:`\texttt{nc} = 1024`, assuming a leading second-order discretization error.

.. math:: \texttt{vf}_\mathrm{ext}=\frac{4}{3}\texttt{vf}_{1024}-\frac{1}{3}\texttt{vf}_{512},

The initialization error :math:`|\texttt{vf}-\texttt{vf}_\mathrm{ext}|` was evaluated for coarser resolutions:

- For :math:`\texttt{nc} = 10`, the error is :math:`6.9 \times 10^{-2}`.

- For :math:`\texttt{nc} = 20`, the computed fraction is :math:`v_f = 0.372632`, yielding an error of :math:`1.8 \times 10^{-2}`.

The convergence order is estimated as:

.. math:: p \approx \log_2 \left( \frac{6.9 \times 10^{-2}}{1.8 \times 10^{-2}} \right) \approx 1.94

The observed error reduction is consistent with approximately second-order behavior over these two resolutions, using the extrapolated solution as a numerical reference.

4.1.2 Runtime workflow analysis and accuracy validation of PLIC operations
--------------------------------------------------------------------------

.. _sec:assessment:

This section presents a detailed runtime workflow analysis alongside quantitative accuracy results

for various PLIC routines.

Comprehensive assessments of these methods are provided in References [\ :ref:`6 <bib-lopez08>`\ , \ :ref:`7 <bib-lopez13>`\ , \ :ref:`8 <bib-lopez16>`\ , \ :ref:`9 <bib-lopez17>`\ , \ :ref:`10 <bib-lopez18jcp>`\ , \ :ref:`11 <bib-lopez19>`\ , \ :ref:`12 <bib-lopez18cpc>`\ , \ :ref:`15 <bib-lopez21>`\ ].

Volume truncation
~~~~~~~~~~~~~~~~~

Firstly,

the non-convex pentagonal pyramid shown in Fig. \ :ref:`3.2 <cells-paraview>`\ , which is defined by the supplied routine ``voftools_ncpentapy`` (the position coordinates of its vertices are shown in Fig. \ :ref:`4.11 <ncpentapyramid>`\ ), is considered.

.. _ncpentapyramid:

.. figure:: /_images/ncpentapyramid.png
   :alt: Position coordinates of the vertices of the non-convex pentagonal pyramid shown in Fig. 3.2.
   :align: center

   **Figure 4.11.** Position coordinates of the vertices of the non-convex pentagonal pyramid shown in Fig. \ :ref:`3.2 <cells-paraview>`\ .

Table \ :ref:`4.6 <polyhedron-nc-ipv-arrangement>`\  presents the arrangement of the vertices of this polyhedron.

.. _polyhedron-nc-ipv-arrangement:

**Table 4.6.** Array ``ipv0`` of vertex number, :math:`i_p`, assigned to every vertex index :math:`i` of face boundary :math:`j` of the polyhedron of Fig. \ :ref:`4.11 <ncpentapyramid>`\ . Each table entry is ``ipv0(j,i)``.

+---------------+----------------------------------------------------------------------+
| Vertex index  | Face boundary :math:`j`                                              |
+===============+==========+===========+===========+===========+===========+===========+
| 2-7 :math:`i` | 1        | 2         | 3         | 4         | 5         | 6         |
+---------------+----------+-----------+-----------+-----------+-----------+-----------+
| 1             | 1        | 1         | 2         | 3         | 4         | 5         |
+---------------+----------+-----------+-----------+-----------+-----------+-----------+
| 2             | 5        | 2         | 3         | 4         | 5         | 1         |
+---------------+----------+-----------+-----------+-----------+-----------+-----------+
| 3             | 4        | 6         | 6         | 6         | 6         | 6         |
+---------------+----------+-----------+-----------+-----------+-----------+-----------+
| 4             | 3        | :math:`-` | :math:`-` | :math:`-` | :math:`-` | :math:`-` |
+---------------+----------+-----------+-----------+-----------+-----------+-----------+
| 5             | 2        | :math:`-` | :math:`-` | :math:`-` | :math:`-` | :math:`-` |
+---------------+----------+-----------+-----------+-----------+-----------+-----------+

Fig. \ :ref:`4.12 <ncpentapyramid-cut>`\  shows the truncation operation, performed by calling the routine ``inte3d`` (Section \ :ref:`3.7 <sec:inte3d>`\ ), over the considered polyhedron and

the plane :math:`\mathcal{P}` with interface orientation :math:`\boldsymbol{n}` given by :math:`\texttt{xnc}=0`, :math:`\texttt{ync}=-1` and :math:`\texttt{znc}=0`, and position given by :math:`\texttt{c}=0.18`.

.. _ncpentapyramid-cut:

.. figure:: /_images/ncpentapyramid-cut.png
   :alt: Truncation of the polyhedron \Omega of Fig. 4.11 (dotted lines) by a plane \mathcal{P} defined by \texttt{xnc}=0, \texttt{ync}=-1, \texttt{znc}=0 and \texttt{c}=0.18
   :align: center

   **Figure 4.12.** Truncation of the polyhedron :math:`\Omega` of Fig. \ :ref:`4.11 <ncpentapyramid>`\  (dotted lines) by a plane :math:`\mathcal{P}` defined by :math:`\texttt{xnc}=0`, :math:`\texttt{ync}=-1`, :math:`\texttt{znc}=0` and :math:`\texttt{c}=0.18`

(highlighted in gray). The truncated polyhedron :math:`\Omega_T` is represented with blue thick lines.

Internally, an auxiliary array ``ia`` of length ``nv`` is constructed to store the information of the position of each vertex with respect to the plane :math:`\mathcal{P}`, where a value equal to 1 indicates that the vertex is located in the half-space defined by :math:`\boldsymbol{n}\cdot\boldsymbol{x}+\texttt{c}>0` and a value equal to 0 indicates that the vertex is located in the half-space defined by :math:`\boldsymbol{n}\cdot\boldsymbol{x}+\texttt{c}\le 0`. The vertices with ``ia`` array values equal to 1 and 0 are represented in Fig. \ :ref:`4.12 <ncpentapyramid-cut>`\  with black and white circles, respectively. As described below, the resulting truncated region :math:`\Omega_T` (thick lines in Fig. \ :ref:`4.12 <ncpentapyramid-cut>`\ ) will be defined by the vertices where the ``ia`` value is equal to 1 and the points of intersection between :math:`\mathcal{P}` and the edges of :math:`\Omega` (:math:`\times` symbols in Fig. \ :ref:`4.12 <ncpentapyramid-cut>`\ ). For example, one of these edges is defined by the two adjacent vertices, :math:`\boldsymbol{x}_5` and :math:`\boldsymbol{x}_4`, and the position vector of the intersection point results as :math:`\boldsymbol{x}_{7}=\boldsymbol{x}_4-\frac{\phi_4}{\phi_5-\phi_4}\,(\boldsymbol{x}_5-\boldsymbol{x}_4),` where :math:`\phi_i=\mathbf{n}\cdot\mathbf{x}_i+\texttt{c}`. The truncation procedure begins by discarding the polyhedron face boundaries in which all the vertices have null value for the array ``ia`` (discarded face boundary :math:`6` in Fig. \ :ref:`4.13 <ncpentapyramid-cut11>`\ ) by setting the corresponding value of array :math:`\texttt{nipv1}` to 0.

.. _ncpentapyramid-cut11:

.. figure:: /_images/ncpentapyramid-cut11.png
   :alt: Face discarding.
   :align: center

   **Figure 4.13.** Face discarding.

Next, the new array ``ipv1`` of ordered vertex indices for every truncated face boundary (face boundaries :math:`1`, :math:`2`, :math:`3`, :math:`4` and :math:`5` in Fig. \ :ref:`4.14 <ncpentapyramid-clipping>`\ ) and every new on-:math:`\mathcal{P}` face boundary of the truncated polyhedron (face boundary :math:`7` in Fig. \ :ref:`4.15 <ncpentapyramid-capping>`\ ) is constructed following, respectively, the clipping and capping procedures described in [\ :ref:`10 <bib-lopez18jcp>`\ ].

.. _ncpentapyramid-clipping:

.. figure:: /_images/ncpentapyramid-clipping.png
   :alt: Clipping procedure
   :align: center

   **Figure 4.14.** Clipping procedure

for the face boundaries (a) :math:`1`, (b) :math:`2`,(c) :math:`3`, (d) :math:`4` and (e) :math:`5` of Fig. \ :ref:`4.12 <ncpentapyramid-cut>`\ . Polygon truncation on the left and truncated polygons, filled with blue (arrows indicate vertex order), on the right.

Fig. \ :ref:`4.15 <ncpentapyramid-capping>`\  illustrates the sequence of the on-:math:`\mathcal{P}` face boundary construction. Intersection vertices are represented with :math:`\times`, truncated faces are gray filled and the polygonal boundary of the constructed on-:math:`\mathcal{P}` face is highlighted at the end of the sequence in blue thick lines. The edge of a truncated face boundary containing a “key vertex” [\ :ref:`10 <bib-lopez18jcp>`\ ] and the edge of that face boundary through which the edges of the on-:math:`\mathcal{P}` face boundaries are sequentially constructed are also highlighted in each picture as :math:`\circ\rightarrow\bullet`   and :math:`\bullet\rightarrow\circ`, respectively.

In this example, the resulting on-plane face boundary is a weakly simple polygonal chain. Edges 7-10 and 9-8 partially overlap and traverse their common portion in opposite directions, allowing the two disjoint coplanar regions (highlighted in blue in Fig. \ :ref:`4.16 <ncpentapyramid-onp>`\ ) to be represented by a single closed chain as :math:`\texttt{ipv1}(7,i)=(7,10,11,9,8,12)` for :math:`i=1` to :math:`\texttt{nipv1}(7)=6` (Fig. \ :ref:`4.16 <ncpentapyramid-onp>`\  shows this arrangement). Table \ :ref:`4.7 <polyhedron-cut-arrangement>`\  shows the vertex arrangement of the polyhedron, :math:`\Omega_T`, resulting from the truncation operation of Fig. \ :ref:`4.12 <ncpentapyramid-cut>`\ .

.. _polyhedron-cut-arrangement:

**Table 4.7.** Array ``ipv1`` of the index number, :math:`i_p`, assigned to every vertex index :math:`i` of face boundary :math:`j` of the polyhedron, :math:`\Omega_T`, resulting from the truncation operation of Fig. \ :ref:`4.12 <ncpentapyramid-cut>`\ . Each table entry is ``ipv1(j,i)``.

+---------------+---------------------------------------------------------------------------+
| Vertex index  | Face boundary :math:`j`                                                   |
+===============+=======+===========+===========+===========+===========+===========+=======+
| 2-8 :math:`i` | 1     | 2         | 3         | 4         | 5         | 6         | 7     |
+---------------+-------+-----------+-----------+-----------+-----------+-----------+-------+
| 1             | 7     | 10        | 2         | 8         | 4         | :math:`-` | 7     |
+---------------+-------+-----------+-----------+-----------+-----------+-----------+-------+
| 2             | 4     | 2         | 9         | 4         | 7         | :math:`-` | 10    |
+---------------+-------+-----------+-----------+-----------+-----------+-----------+-------+
| 3             | 8     | 11        | 11        | 12        | 12        | :math:`-` | 11    |
+---------------+-------+-----------+-----------+-----------+-----------+-----------+-------+
| 4             | 9     | :math:`-` | :math:`-` | :math:`-` | :math:`-` | :math:`-` | 9     |
+---------------+-------+-----------+-----------+-----------+-----------+-----------+-------+
| 5             | 2     | :math:`-` | :math:`-` | :math:`-` | :math:`-` | :math:`-` | 8     |
+---------------+-------+-----------+-----------+-----------+-----------+-----------+-------+
| 6             | 10    | :math:`-` | :math:`-` | :math:`-` | :math:`-` | :math:`-` | 12    |
+---------------+-------+-----------+-----------+-----------+-----------+-----------+-------+

.. _ncpentapyramid-capping:

.. figure:: /_images/ncpentapyramid-capping.png
   :alt: Sequence (from top to bottom and from left to right) of the capping procedure applied for the construction of the on-\mathcal{P} face boundary (thick lines) in the example of Fig. 4.12.
   :align: center

   **Figure 4.15.** Sequence (from top to bottom and from left to right) of the capping procedure applied for the construction of the on-:math:`\mathcal{P}` face boundary (thick lines) in the example of Fig. \ :ref:`4.12 <ncpentapyramid-cut>`\ .

.. _ncpentapyramid-onp:

.. figure:: /_images/ncpentapyramid-onp.png
   :alt: Vertex arrangement of the on-\mathcal{P} face boundary in the example of Fig. 4.12.
   :align: center

   **Figure 4.16.** Vertex arrangement of the on-:math:`\mathcal{P}` face boundary in the example of Fig. \ :ref:`4.12 <ncpentapyramid-cut>`\ .

.. _ncsicosahedron-4newfaces:

.. figure:: /_images/ncsicosahedron-4newfaces.png
   :alt: Example of the truncation between the stellated icosahedron of Fig. 3.2
   :align: center

   **Figure 4.17.** Example of the truncation between the stellated icosahedron of Fig. \ :ref:`3.2 <cells-paraview>`\ 

and a half-space that produces four new on-:math:`\mathcal{P}` face boundaries (black thick lines). The truncated regions are highlighted in blue.

A case in which the application of the capping procedure produces multiple new on-:math:`\mathcal{P}` face boundaries (four in total) can be seen in Fig. \ :ref:`4.17 <ncsicosahedron-4newfaces>`\ .

Volume conservation enforcement in PLIC reconstruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Figs. \ :ref:`4.18 <vce-sequence>`\  and \ :ref:`4.19 <vce-sequenceb>`\  show the sequence of application of the VCE operation, performed by calling the routine ``enforv3d``, over the cell of Fig. \ :ref:`4.11 <ncpentapyramid>`\  for a case with PLIC interface orientation :math:`\boldsymbol{n}` given by :math:`\texttt{xnc}=0`, :math:`\texttt{ync}=-1` and :math:`\texttt{znc}=0`, and ratio between the reference material and cell volumes (volume fraction ``f``) :math:`\texttt{v}/\texttt{vt}=0.55` (a sketch of the flow diagram of the VCE operation is also included in the figures to

highlight the applied steps). The sequence for this case occurs as follows. [2]_

.. _vce-sequence:

.. figure:: /_images/vce-sequence.png
   :alt: Sequence of application of the VCE operation in a PLIC reconstruction within the cell of Fig. 4.11 for a case with \texttt{xnc}=0, \texttt{ync}=-1, \texttt{znc}=0 and \texttt{f}=\texttt{v/vt}=0.55. (a) First tentative value of the solution and identification of the bracketing interval. (b) Computation of the coefficients of the analytical function \texttt{v(c)} valid inside the tentative bracketing interval, from which the bounds \texttt{vmax} and \texttt{vmin} are obtained, and check if the condition \texttt{vmin}\le \texttt{v} < \texttt{vmax} is or not satisfied.
   :align: center

   **Figure 4.18.** Sequence of application of the VCE operation in a PLIC reconstruction within the cell of Fig. \ :ref:`4.11 <ncpentapyramid>`\  for a case with :math:`\texttt{xnc}=0`, :math:`\texttt{ync}=-1`, :math:`\texttt{znc}=0` and :math:`\texttt{f}=\texttt{v/vt}=0.55`. (a) First tentative value of the solution and identification of the bracketing interval. (b) Computation of the coefficients of the analytical function :math:`\texttt{v(c)}` valid inside the tentative bracketing interval, from which the bounds :math:`\texttt{vmax}` and :math:`\texttt{vmin}` are obtained, and check if the condition :math:`\texttt{vmin}\le \texttt{v} < \texttt{vmax}` is or not satisfied.

.. _vce-sequenceb:

.. figure:: /_images/vce-sequenceb.png
   :alt: Continuation of the sequence of Fig. 4.18. (a) Steps (i) to (iii) are repeated and the volume condition is checked again. (b) The volume condition is satisfied and the final solution is analytically obtained.
   :align: center

   **Figure 4.19.** Continuation of the sequence of Fig. \ :ref:`4.18 <vce-sequence>`\ . (a) Steps (i) to (iii) are repeated and the volume condition is checked again. (b) The volume condition is satisfied and the final solution is analytically obtained.

#. For this geometry and normal direction, the initial bounds are :math:`\texttt{c}=0` and :math:`\texttt{c}=1`, corresponding to empty and full cells, respectively. Linear interpolation (see Fig. \ :ref:`4.18 <vce-sequence>`\ (a)) between these bounds therefore gives:

   .. math:: \texttt{ct1}=\frac{\texttt{v}}{\texttt{vt}}=0.55.

#. The section of the function :math:`\texttt{v}(\texttt{c})` that satisfies the condition :math:`\texttt{cmin}\le \texttt{ct1}< \texttt{cmax}` is searched (Fig. \ :ref:`4.18 <vce-sequence>`\ (b)). The identified section is delimited by the tentative bracket values :math:`\texttt{cmin}=0.5` and :math:`\texttt{cmax}=0.77` (these values correspond to the constant of the planar interfaces passing through vertices :math:`6` (thus, :math:`\texttt{cmin}=-\texttt{xnc} \times \texttt{vertp(6,1)}-\texttt{ync} \times \texttt{vertp(6,2)}-\texttt{znc} \times \texttt{vertp(6,3)}`) and :math:`1` (thus, :math:`\texttt{cmax}=-\texttt{xnc} \times \texttt{vertp(1,1)}-\texttt{ync} \times \texttt{vertp(1,2)}-\texttt{znc} \times \texttt{vertp(1,3)}`)) and the corresponding coefficients of the function :math:`\texttt{v(c)/vt}` are obtained from the analytical relations given in [\ :ref:`10 <bib-lopez18jcp>`\ ], resulting for this section as (the coefficients are displayed to five decimal places)

   .. math:: \frac{\texttt{v(c)}}{\texttt{vt}}=1.36248 \texttt{c}^3-5.41244 \texttt{c}^2+6.43269 \texttt{c}-1.40609.

   From the above expression, the bounds of the first tentative bracket are

   .. math:: \frac{\texttt{vmax}}{\texttt{vt}}=0.96006

   and

   .. math:: \frac{\texttt{vmin}}{\texttt{vt}}=0.62745.

   Note that the tentative bracket determined by these bounds does not contain the value :math:`\texttt{v/vt}=0.55` and a new tentative interpolation bracketing must be carried out.

#. A second tentative value, ``ct2``, is obtained by using the linear interpolation shown in Fig. \ :ref:`4.19 <vce-sequenceb>`\ (a) for which the upper limit of the interpolation line has been moved to the point on the curve :math:`\texttt{v(c)/vt}` corresponding to :math:`\texttt{c}=0.5`. In this way, the new interpolated tentative value results as

   .. math:: \texttt{ct2}=0.43828.

   The section of the function :math:`\texttt{v(c)}` that satisfies the condition :math:`\texttt{cmin}\le \texttt{ct2}<\texttt{cmax}` is now delimited by the planar interfaces passing through vertices :math:`6` (thus, :math:`\texttt{cmax}=-\texttt{xnc} \times \texttt{vertp(6,1)}-\texttt{ync} \times \texttt{vertp(6,2)}-\texttt{znc} \times \texttt{vertp(6,3)}=0.5`) and :math:`3` (thus, :math:`\texttt{cmin}=-\texttt{xnc} \times \texttt{vertp(3,1)}-\texttt{ync} \times \texttt{vertp(3,2)}-\texttt{znc} \times \texttt{vertp(3,3)}=0.22`) and the corresponding analytical expression of :math:`\texttt{v(c)/vt}` for this section results from [\ :ref:`10 <bib-lopez18jcp>`\ ] as

   .. math:: \frac{\texttt{v(c)}}{\texttt{vt}}=-12.29024 \texttt{c}^3+15.06660 \texttt{c}^2-3.80685 \texttt{c}+0.30050.

   The bounds of the second tentative bracket are

   .. math:: \frac{\texttt{vmax}}{\texttt{vt}}=0.62745

   and

   .. math:: \frac{\texttt{vmin}}{\texttt{vt}}=0.06135.

   This tentative bracket includes the value :math:`\texttt{v/vt}=0.55`.

#. The final solution is analytically computed (Fig. \ :ref:`4.19 <vce-sequenceb>`\ (b)) as indicated in [\ :ref:`6 <bib-lopez08>`\ ], resulting

   .. math:: \texttt{c}=0.46394.

Operations over a non-convex polyhedron with disjoint regions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _voftoolslogo-f:

.. figure:: /_images/voftoolslogo-f.png
   :alt: Liquid volume regions (blue color) obtained from the intersection between the VOFTools logo cell (routine voftools_logo; see Fig. 3.2) and half-spaces defined by planes that contain the PLIC interfaces with normal vector \vec{n}=(0,-1,0) and different liquid volume fractions v/vt (the solutions of the VCE problem are included in parenthesis). The original cell is depicted on each picture using partial transparent gray.
   :align: center

   **Figure 4.20.** Liquid volume regions (blue color) obtained from the intersection between the ``VOFTools`` logo cell (routine ``voftools_logo``; see Fig. \ :ref:`3.2 <cells-paraview>`\ ) and half-spaces defined by planes that contain the PLIC interfaces with normal vector :math:`\boldsymbol{n}=(0,-1,0)` and different liquid volume fractions ``v/vt`` (the solutions of the VCE problem are included in parenthesis). The original cell is depicted on each picture using partial transparent gray.

.. _voftoolslogo-fb:

.. figure:: /_images/voftoolslogo-fb.png
   :alt: Same as in Fig. 4.20 but with \vec{n}=(-1,0,0).
   :align: center

   **Figure 4.21.** Same as in Fig. \ :ref:`4.20 <voftoolslogo-f>`\  but with :math:`\boldsymbol{n}=(-1,0,0)`.

``VOFTools`` also supports non-convex polyhedra with disjoint regions. For these geometries, the retained-volume function ``v(c)`` remains continuous but may contain constant intervals when the cutting plane traverses gaps between regions.

Figs. \ :ref:`4.20 <voftoolslogo-f>`\  and \ :ref:`4.21 <voftoolslogo-fb>`\  show the liquid volume regions (blue color) obtained from the intersection between the ``VOFTools`` logo cell (routine ``voftools_logo``; see Fig. \ :ref:`3.2 <cells-paraview>`\ ), where each letter is represented by a disjoint polyhedral region, and half-spaces defined by planes given by :math:`\boldsymbol{n}\cdot \boldsymbol{x}+\texttt{c}=0` with, respectively, :math:`\boldsymbol{n}=(\texttt{xnc}=0,\texttt{ync}=-1,\texttt{znc}=0)` and :math:`\boldsymbol{n}=(\texttt{xnc}=-1,\texttt{ync}=0,\texttt{znc}=0)`, and the constant ``c`` obtained by solving the VCE problem for

different liquid volume fractions ``f`` (the original cell is depicted on each picture using partial transparent gray). For the orientations in Figs. \ :ref:`4.20 <voftoolslogo-f>`\  and \ :ref:`4.21 <voftoolslogo-fb>`\ , the cutting planes are :math:`y=\texttt{c}` and :math:`x=\texttt{c}`, respectively, and the retained regions satisfy :math:`y<\texttt{c}` and :math:`x<\texttt{c}`. For the orientation used in Fig. \ :ref:`4.21 <voftoolslogo-fb>`\ , gaps between the letters produce constant intervals in ``v(c)`` (Fig. \ :ref:`4.22 <vc-voftoolslogo>`\ ). A target volume corresponding to such an interval admits multiple interface positions.

.. _vc-voftoolslogo:

.. figure:: /_images/vc-voftoolslogo.png
   :alt: Liquid volume fraction \texttt{v}(\texttt{c})/\texttt{vt} as a function of \texttt{c} for the VOFTools logo cell and an interface orientation given by \vec{n}=(-1,0,0).
   :align: center

   **Figure 4.22.** Liquid volume fraction :math:`\texttt{v}(\texttt{c})/\texttt{vt}` as a function of :math:`\texttt{c}` for the ``VOFTools`` logo cell and an interface orientation given by :math:`\boldsymbol{n}=(-1,0,0)`.

Volume fraction initialization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _test-initf:

.. figure:: /_images/test-initf.png
   :alt: Liquid volume initialization of a circular and spherical liquid body (blue color) with radius r_l=0.325 in the non-convex cell of Fig. 3.1 defined by the routine voftools_hsquare (top picture) and the non-convex cell of Fig. 3.2 defined by the routine voftools_hcube (bottom picture).
   :align: center

   **Figure 4.23.** Liquid volume initialization of a circular and spherical liquid body (blue color) with radius :math:`r_l=0.325` in the non-convex cell of Fig. \ :ref:`3.1 <cells-gnuplot>`\  defined by the routine ``voftools_hsquare`` (top picture) and the non-convex cell of Fig. \ :ref:`3.2 <cells-paraview>`\  defined by the routine ``voftools_hcube`` (bottom picture).

The accuracy of several initialization operations, performed by calling the routines ``initf2d`` (Section \ :ref:`3.29 <sec:initf2d>`\ ) for 2D and ``initf3d`` (Section \ :ref:`3.19 <sec:initf3d>`\ ) for 3D cases, is also assessed. Firstly, the following two cases with non-convex cells (see Fig. \ :ref:`4.23 <test-initf>`\ ) are considered:

#. Initialization of a circular liquid body with radius :math:`r_l` centered at the center of the cell in a unit-length square with a half-length square hole located at its center (top picture in Fig. \ :ref:`4.23 <test-initf>`\ ). The exact area fraction of liquid inside the cell can be obtained as

   .. math:: \texttt{vf}_\mathrm{exact}=\frac{2^3}{3}r_l^2\left(\theta-\sin \theta \right),

   where :math:`\theta=2\arccos\left[1/(2^2r_l)\right]` and :math:`2^{-2}\le r_l \le 2^{-3/2}`.

#. Initialization of a spherical liquid body with radius :math:`r_l` centered at the center of the cell in a unit-length cube with a half-length cubic hole located at its center (bottom picture in Fig. \ :ref:`4.23 <test-initf>`\ ). The exact volume fraction of liquid inside the cell can be obtained as

   .. math:: \texttt{vf}_\mathrm{exact}=\frac{2^4}{7} \pi \left(r_l - 2^{-2} \right)^2 \left(2r_l +2^{-2} \right),

   with :math:`2^{-2}\le r_l \le 2^{-3/2}`.

Fig. \ :ref:`4.24 <initf-errors>`\  shows the initialization error

.. math:: |\texttt{vf}-\texttt{vf}_\mathrm{exact}|

as a function of the number of divisions ``nc`` for these 2D and 3D cases with :math:`r_l=0.325` (both liquid bodies are defined by calling the functions ``func2d1`` and ``func3d1``). For these and the remaining initialization tests, the threshold parameter ``tol`` is chosen sufficiently large to bypass the preliminary full/empty classification and activate Cartesian subdivision

(see Reference [\ :ref:`10 <bib-lopez18jcp>`\ ] for a more detailed discussion about this threshold parameter). It can be observed that the results tend to reach the exact solution with a second-order convergence rate.

.. _initf-errors:

.. figure:: /_images/initf-errors.png
   :alt: Initialization errors as a function of nc for the 2D and 3D cases of Fig. 4.23.
   :align: center

   **Figure 4.24.** Initialization errors as a function of ``nc`` for the 2D and 3D cases of Fig. \ :ref:`4.23 <test-initf>`\ .

.. _initf-ellipse-torus:

.. figure:: /_images/initf-ellipse-torus.png
   :alt: Examples for the initialization of the material bodies of Eq. (4.1) (left column) and Eq. (4.2) (right column) in several cells of Fig. 3.1 and Fig. 3.2, respectively.
   :align: center

   **Figure 4.25.** Examples for the initialization of the material bodies of Eq. (\ :ref:`4.1 <ellipse>`\ ) (left column) and Eq. (\ :ref:`4.2 <torus>`\ ) (right column) in several cells of Fig. \ :ref:`3.1 <cells-gnuplot>`\  and Fig. \ :ref:`3.2 <cells-paraview>`\ , respectively.

The accuracy of the initialization procedure for more complex cases, for which obtaining the exact solution analytically is not an easy task, has been obtained using the Richardson extrapolation method [\ :ref:`2 <bib-celik95>`\ ]. Two material bodies with elliptical and toroidal interfaces defined by calling the functions ``func2d2`` and ``func3d2``

are given as a function of :math:`x`, :math:`y`, :math:`z`-coordinates by, respectively,

.. _ellipse:

.. math::

   f(x,y)=1-\left[\left(\frac{x-0.5}{0.5}\right)^2+\left(\frac{y-0.5}{0.2}\right)^2\right] \tag{4.1}

and

.. _torus:

.. math::

   f(x,y,z)=\left(\frac{1}{3} \right)^2 - \left\{ \frac{2}{3}-\left[(x-0.5)^2+(z-0.5)^2\right]^{0.5}\right\}^2-(y-0.5)^2. \tag{4.2}

.. _initf-errors-ellipse-torus:

.. figure:: /_images/initf-errors-ellipse-torus.png
   :alt: Initialization errors as a function of nc for several non-convex cells of Figs. 3.1 and 3.2 and the material bodies with (a) elliptical shape of Eq. (4.1) and (b) toroidal shape of Eq. (4.2), respectively.
   :align: center

   **Figure 4.26.** Initialization errors as a function of ``nc`` for several non-convex cells of Figs. \ :ref:`3.1 <cells-gnuplot>`\  and \ :ref:`3.2 <cells-paraview>`\  and the material bodies with (a) elliptical shape of Eq. (\ :ref:`4.1 <ellipse>`\ ) and (b) toroidal shape of Eq. (\ :ref:`4.2 <torus>`\ ), respectively.

Fig. \ :ref:`4.25 <initf-ellipse-torus>`\  shows the above material bodies along with several cells of Figs. \ :ref:`3.1 <cells-gnuplot>`\  (left column) and \ :ref:`3.2 <cells-paraview>`\  (right column). The accuracy is quantified assuming a leading second-order discretization error through the error defined as

.. math:: |\texttt{vf}-\texttt{vf}_\mathrm{ext}|,

where :math:`\texttt{vf}_\mathrm{ext}` is the extrapolated numerical solution [\ :ref:`2 <bib-celik95>`\ ] obtained as

.. math:: \texttt{vf}_\mathrm{ext}=\frac{4}{3} \texttt{vf}_{1024} - \frac{1}{3} \texttt{vf}_{512}

where :math:`\texttt{vf}_{1024}` and :math:`\texttt{vf}_{512}` are numerical results obtained on finer grids.

The error curves in Fig. \ :ref:`4.26 <initf-errors-ellipse-torus>`\  exhibit approximately second-order behavior over the displayed refinement range, using the extrapolated solutions as numerical references.

.. [1]
   The distance calculation in these test programs is restricted to convex cells. For non-convex cells, the interface may consist of multiple segments or non-convex or disconnected polygonal regions, requiring additional geometric processing. The ``dist2d`` routine handles a single segment, whereas ``dist3d`` requires a planar convex polygon.

.. [2]
   For clarity in the explanation of this example, it has been omitted the activation, when appropriate to achieve a better computational efficiency, of the solution of

   .. math:: \texttt{v}(\texttt{c})-(\texttt{vt}-\texttt{v})=0,

   with interface normal :math:`-\boldsymbol{n}`, instead of the solution of :math:`\texttt{v}(\texttt{c})-\texttt{v}=0` with interface normal :math:`\boldsymbol{n}` (see Reference [\ :ref:`8 <bib-lopez16>`\ ] for the details).
