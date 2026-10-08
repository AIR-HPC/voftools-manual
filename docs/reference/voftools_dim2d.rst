3.31 ``voftools_dim2d`` – Retrieve array dimensioning parameter for 2D polygons
===============================================================================

The ``voftools_dim2d`` routine returns the vertex-array dimensioning parameter ``nv`` compiled into the library. This value specifies storage capacity, rather than the actual number of vertices of a particular polygon.

**Fortran:**

.. code:: fortran

   call voftools_dim2d(nv)

**C:**

.. code:: c

   voftools_dim2d(&nv);

**Python:**

.. code:: python

   nv = voft.voftools_dim2d()

**Argument:**

====== ======= ======= ============================================
``nv`` ``OUT`` ``I_P`` compiled storage capacity for vertex entries
====== ======= ======= ============================================

**Note:** Storage must accommodate any additional vertices generated during geometric operations. This routine only reports the compiled dimension; changing it requires rebuilding the library.
