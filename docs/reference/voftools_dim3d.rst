3.21 ``voftools_dim3d`` – Retrieve array dimensioning parameters for 3D polyhedra
=================================================================================

The ``voftools_dim3d`` routine returns the array dimensioning parameters ``ns`` and ``nv`` compiled into the library. These values specify storage capacities, rather than the actual numbers of faces and vertices of a particular polyhedron.

**Fortran:**

.. code:: fortran

   call voftools_dim3d(ns,nv)

**C:**

.. code:: c

   voftools_dim3d(&ns,&nv);

**Python:**

.. code:: python

   (ns,nv) = voft.voftools_dim3d()

**Arguments:**

====== ======= ======= ============================================
``ns`` ``OUT`` ``I_P`` compiled storage capacity for face entries
``nv`` ``OUT`` ``I_P`` compiled storage capacity for vertex entries
====== ======= ======= ============================================

**Note:** Storage must accommodate any additional faces and vertices generated during geometric operations. This routine only reports the compiled dimensions; changing them requires rebuilding the library.
