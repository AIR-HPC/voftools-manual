3.3 ``defpol3d`` – Initialize polyhedron type
=============================================

The ``defpol3d`` routine selects one of the polyhedral geometries shown in Fig. \ :ref:`3.2 <cells-paraview>`\ , determined by the integer parameter ``icelltype`` (see Table \ :ref:`3.4 <geometries-index>`\ ).

.. _geometries-index:

**Table 3.4.** Values of the index used to denote the cell geometry routines considered in the test programs.

======================= =======================
**Routine name**        **``icelltype`` index**
======================= =======================
\                       *3D geometries*
``voftools_cube``       11
``voftools_ihexa``      12
``voftools_tetra``      13
``voftools_dodeca``     14
``voftools_icosa``      15
``voftools_ipol3d``     16
``voftools_ncpentapy``  111
``voftools_nccubepy``   112
``voftools_scube``      113
``voftools_nchexa``     114
``voftools_sdodeca``    115
``voftools_sicosa``     116
``voftools_hcube``      117
``voftools_drcube``     118
``voftools_zigzag``     119
``voftools_logo``       120
\                       *2D geometries*
``voftools_square``     1
``voftools_hexagon``    2
``voftools_tri``        3
``voftools_quad``       4
``voftools_pentagon``   5
``voftools_ihexagon``   6
``voftools_ncquad``     101
``voftools_ncpentagon`` 102
``voftools_nchexagon``  103
``voftools_shexagon``   104
``voftools_hsquare``    105
``voftools_msquare``    106
======================= =======================

The calling conventions for this routine in Fortran, C, and Python are as follows:

**Fortran:**

.. code:: fortran

   call defpol3d(icelltype,ipv,nipv,ntp,nts,ntv,vertp,xns,yns,zns)

**C:**

.. code:: c

   defpol3d(&icelltype,ipv,nipv,&ntp,&nts,&ntv,vertp,xns,yns,zns);

**Python:**

.. code:: python

   (ipv,nipv,ntp,nts,ntv,vertp,xns,yns,zns)=voft.defpol3d(icelltype)

**Arguments:**

+-------------------+---------+---------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``icelltype``     | ``IN``  | ``I_P`` | cell geometry index                                                                                                                          |
+-------------------+---------+---------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``ipv``           | ``OUT`` | ``I_P`` | array of dimensions ``(ns,nv)`` storing the vertex indices defining each face boundary                                                       |
+-------------------+---------+---------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``nipv``          | ``OUT`` | ``I_P`` | array of length :math:`\texttt{ns}` storing the number of vertices per face boundary                                                         |
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

**Note:** The ``defpol3d`` routine, used by the ``test3d`` program to select predefined cells, accepts ``icelltype`` values 11–16 for convex cells and 111–120 for non-convex cells. This selection does not restrict users to these geometries: user-defined polyhedral cells can be supplied directly to the relevant ``VOFTools`` routines through their vertex coordinates, face connectivity, and outward-pointing unit face normals, subject to each routine’s requirements and the compiled array capacities. An invalid ``icelltype`` value causes ``defpol3d`` to print a diagnostic message and terminate the program through a Fortran ``STOP`` statement, including when called from C or Python.
