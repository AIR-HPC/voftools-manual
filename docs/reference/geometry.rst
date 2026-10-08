3.2 Polyhedron and polygon geometries
=====================================

``VOFTools`` allows for the representation of arbitrary convex and non-convex polyhedral and polygonal geometries.

While Table \ :ref:`3.3 <geometries-description>`\  summarizes the specific cell types implemented in the test programs of Section \ :ref:`4 <sec:test-program>`\ , the core library enables users to define arbitrary polytopes beyond this predefined set. These geometries are defined by invoking specific initialization routines that return the necessary geometric parameters.

.. _cells-gnuplot:

.. figure:: /_images/cells-gnuplot.png
   :alt: Cell geometries for the 2D cases of Table 3.3.
   :align: center

   **Figure 3.1.** Cell geometries for the 2D cases of Table \ :ref:`3.3 <geometries-description>`\ .

The geometry of polyhedra and polygons is represented using connectivity arrays and coordinate lists. To maintain compatibility with fixed-dimension buffers and avoid jagged array complexities, these quantities are physically allocated with a maximum capacity ``ns`` (for faces) or ``nv`` (for vertices). However, their logical sizes correspond to the actual number of entities (e.g., :math:`\texttt{nts}` for face boundaries and :math:`\texttt{ntv}` for vertices). This convention ensures that routines operate on logical arrays of the appropriate size while respecting the allocated physical buffers of size ``ns`` or ``nv``.

Figs. \ :ref:`3.1 <cells-gnuplot>`\  and \ :ref:`3.2 <cells-paraview>`\  illustrate representative cells using the ``polout2d`` (Section \ :ref:`3.30 <polout2d>`\ ) and ``polout3d`` (Section \ :ref:`3.20 <polout3d>`\ ) visualization routines in conjunction with ``Gnuplot`` [\ :ref:`16 <bib-gnuplot>`\ ] and ``ParaView`` [\ :ref:`3 <bib-paraview>`\ ], respectively. The routine name corresponding to each geometry is indicated within the figures.

.. _cells-paraview:

.. figure:: /_images/cells-paraview.png
   :alt: Cell geometries for the 3D cases of Table 3.3.
   :align: center

   **Figure 3.2.** Cell geometries for the 3D cases of Table \ :ref:`3.3 <geometries-description>`\ .

As an example, the calling conventions for a cubic cell are provided below for Fortran (blue background), C (green background) and Python (red background):

**Fortran:**

.. code:: fortran

   call voftools_cube(ipv,nipv,ntp,nts,ntv,vertp,xns,yns,zns)

**C:**

.. code:: c

   voftools_cube(ipv,nipv,&ntp,&nts,&ntv,vertp,xns,yns,zns);

**Python:**

.. code:: python

   (ipv,nipv,ntp,nts,ntv,vertp,xns,yns,zns) = voft.voftools_cube()

.. _ncpentapyramid2:

.. figure:: /_images/ncpentapyramid2.png
   :alt: Detailed definition of the non-convex pentagonal pyramid shown in Fig. 3.2. See the source code of the routine voftools_ncpentapy for parameter definitions. Note that the values of the face normal components (xns, yns, zns) are rounded in the figure for clarity. The red arrow indicates the counterclockwise order of the vertices for face boundary 2 when viewed from the exterior of the polyhedron, consistent with the outward-pointing normal convention.
   :align: center

   **Figure 3.3.** Detailed definition of the non-convex pentagonal pyramid shown in Fig. \ :ref:`3.2 <cells-paraview>`\ . See the source code of the routine ``voftools_ncpentapy`` for parameter definitions. Note that the values of the face normal components (``xns``, ``yns``, ``zns``) are rounded in the figure for clarity. The red arrow indicates the counterclockwise order of the vertices for face boundary 2 when viewed from the exterior of the polyhedron, consistent with the outward-pointing normal convention.

**Arguments:**

+-------------------+---------+---------+----------------------------------------------------------------------------------------------------------------------------------------------+
| Argument          | Intent  | Type    | Definition                                                                                                                                   |
+===================+=========+=========+==============================================================================================================================================+
| ``ipv``           | ``OUT`` | ``I_P`` | array of dimensions :math:`(\texttt{ns},\texttt{nv})` storing the vertex indices defining each face boundary                                 |
+-------------------+---------+---------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``nipv``          | ``OUT`` | ``I_P`` | array of length :math:`{\texttt{ns}}` storing the number of vertices per face boundary                                                       |
+-------------------+---------+---------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``ntp``           | ``OUT`` | ``I_P`` | maximum vertex index in the connectivity list                                                                                                |
+-------------------+---------+---------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``nts``           | ``OUT`` | ``I_P`` | total number of face boundaries                                                                                                              |
+-------------------+---------+---------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``ntv``           | ``OUT`` | ``I_P`` | total number of vertices                                                                                                                     |
+-------------------+---------+---------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``vertp``         | ``OUT`` | ``W_P`` | array of dimensions :math:`({nv},3)` storing the :math:`x,y,z`-coordinates of each vertex                                                    |
+-------------------+---------+---------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``xns, yns, zns`` | ``OUT`` | ``W_P`` | arrays of length :math:`\texttt{ns}` storing the :math:`x,y,z`-components of the outward-pointing unit normal vectors for each face boundary |
+-------------------+---------+---------+----------------------------------------------------------------------------------------------------------------------------------------------+

To illustrate a specific example, Fig. \ :ref:`3.3 <ncpentapyramid2>`\  depicts the non-convex pentagonal pyramid defined by the supplied routine ``voftools_ncpentapy`` (also shown in Fig. \ :ref:`3.2 <cells-paraview>`\ ).

For a square cell,

**Fortran:**

.. code:: fortran

   call voftools_square(ipv,ntp,ntv,vertp)

**C:**

.. code:: c

   voftools_square(ipv,&ntp,&ntv,vertp);

**Python:**

.. code:: python

   (ipv,ntp,ntv,vertp) = voft.voftools_square()

**Arguments:**

+-----------+---------+---------+-----------------------------------------------------------------------------------------+
| Argument  | Intent  | Type    | Definition                                                                              |
+===========+=========+=========+=========================================================================================+
| ``ipv``   | ``OUT`` | ``I_P`` | array of length :math:`\texttt{nv}` storing the vertex indices defining the polygon     |
+-----------+---------+---------+-----------------------------------------------------------------------------------------+
| ``ntp``   | ``OUT`` | ``I_P`` | maximum vertex index in the connectivity list                                           |
+-----------+---------+---------+-----------------------------------------------------------------------------------------+
| ``ntv``   | ``OUT`` | ``I_P`` | total number of vertices                                                                |
+-----------+---------+---------+-----------------------------------------------------------------------------------------+
| ``vertp`` | ``OUT`` | ``W_P`` | array of dimensions :math:`({nv},2)` storing the :math:`x,y`-coordinates of each vertex |
+-----------+---------+---------+-----------------------------------------------------------------------------------------+

.. _note-1-1:

Note 1:
^^^^^^^

Initially, :math:`\texttt{ntp}=\texttt{ntv}` for the defined polytope. However, if subsequent intersection operations are performed on the polytope, these values may diverge for the resulting truncated geometry. This is because :math:`\texttt{ntp}` tracks the maximum vertex index in the connectivity list, while :math:`\texttt{ntv}` counts the total count of unique vertices.

Note 2:
^^^^^^^

For detailed definitions of these parameters and their specific roles within the example geometry-defining routines, please refer to the source code of each respective routine.

Similarly, the arguments and calling conventions for the remaining routines in the ``VOFTools`` library (``voftools.f90``) are described in detail below.

To distinguish variables corresponding to different states of a geometric entity (e.g., before and after an operation), numerical suffixes are appended to the parameter names.
