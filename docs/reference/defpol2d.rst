3.22 ``defpol2d`` – Initialize polygon type
===========================================

The ``defpol2d`` routine initializes the geometry of a polygon by selecting one of the predefined shapes shown in Fig. \ :ref:`3.1 <cells-gnuplot>`\ , based on the integer input parameter ``icelltype`` (see Table \ :ref:`3.3 <geometries-description>`\ ).

**Fortran:**

.. code:: fortran

   call defpol2d(icelltype,ipv,ntp,ntv,vertp)

**C:**

.. code:: c

   defpol2d(&icelltype,ipv,&ntp,&ntv,vertp);

**Python:**

.. code:: python

   (ipv,ntp,ntv,vertp)=voft.defpol2d(icelltype)

+---------------+---------+---------+-----------------------------------------------------------------------------------------+
| ``icelltype`` | ``IN``  | ``I_P`` | cell geometry index                                                                     |
+---------------+---------+---------+-----------------------------------------------------------------------------------------+
| ``ipv``       | ``OUT`` | ``I_P`` | array of length ``nv`` storing the vertex indices defining the polygon                  |
+---------------+---------+---------+-----------------------------------------------------------------------------------------+
| ``ntp``       | ``OUT`` | ``I_P`` | maximum vertex index in the connectivity list                                           |
+---------------+---------+---------+-----------------------------------------------------------------------------------------+
| ``ntv``       | ``OUT`` | ``I_P`` | total number of vertices                                                                |
+---------------+---------+---------+-----------------------------------------------------------------------------------------+
| ``vertp``     | ``OUT`` | ``W_P`` | array of dimensions :math:`({nv},2)` storing the :math:`x,y`-coordinates of each vertex |
+---------------+---------+---------+-----------------------------------------------------------------------------------------+

**Note:** The ``defpol2d`` routine, used by the ``test2d`` program to select predefined cells, accepts ``icelltype`` values 1–6 for convex cells and 101–106 for non-convex cells. This selection does not restrict users to these geometries: user-defined polygonal cells can be supplied directly to the relevant ``VOFTools`` routines through their vertex coordinates and connectivity, subject to each routine’s requirements and the compiled array capacities. An invalid ``icelltype`` value causes ``defpol2d`` to print a diagnostic message and terminate the program through a Fortran ``STOP`` statement, including when called from C or Python.
