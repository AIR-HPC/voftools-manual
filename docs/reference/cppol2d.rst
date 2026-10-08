3.27 ``cppol2d`` – Polygon deep copy
====================================

The ``cppol2d`` routine creates a deep copy of a polygon’s geometric and topological structure. It duplicates both the connectivity information (vertex indices) and the vertex coordinates, ensuring that the resulting polygon is an independent data structure from the original.

**Fortran:**

.. code:: fortran

   call cppol2d(ipv0,ipv,ntp0,ntp,ntv0,ntv,vertp0,vertp)

**C:**

.. code:: c

   cppol2d(ipv0,ipv,&ntp0,&ntp,&ntv0,&ntv,vertp0,vertp);

**Python:**

.. code:: python

   (ipv, ntp, ntv, vertp) = voft.cppol2d(ipv0, ntp0, ntv0, vertp0)

**Arguments:**

+------------+---------+---------+-----------------------------------------------------------------------------------------------------------------+
| ``ipv``    | ``OUT`` | ``I_P`` | array of length :math:`\texttt{nv}` storing the vertex indices defining the copied polygon                      |
+------------+---------+---------+-----------------------------------------------------------------------------------------------------------------+
| ``ipv0``   | ``IN``  | ``I_P`` | array of length :math:`\texttt{nv}` storing the vertex indices defining the original polygon                    |
+------------+---------+---------+-----------------------------------------------------------------------------------------------------------------+
| ``ntp``    | ``OUT`` | ``I_P`` | maximum vertex index in the connectivity list of the copied polygon                                             |
+------------+---------+---------+-----------------------------------------------------------------------------------------------------------------+
| ``ntp0``   | ``IN``  | ``I_P`` | maximum vertex index in the connectivity list of the original polygon                                           |
+------------+---------+---------+-----------------------------------------------------------------------------------------------------------------+
| ``ntv``    | ``OUT`` | ``I_P`` | total number of vertices in the copied polygon                                                                  |
+------------+---------+---------+-----------------------------------------------------------------------------------------------------------------+
| ``ntv0``   | ``IN``  | ``I_P`` | total number of vertices in the original polygon                                                                |
+------------+---------+---------+-----------------------------------------------------------------------------------------------------------------+
| ``vertp``  | ``OUT`` | ``W_P`` | array of dimensions :math:`({nv},2)` storing the :math:`x,y`-coordinates of each vertex of the copied polygon   |
+------------+---------+---------+-----------------------------------------------------------------------------------------------------------------+
| ``vertp0`` | ``IN``  | ``W_P`` | array of dimensions :math:`({nv},2)` storing the :math:`x,y`-coordinates of each vertex of the original polygon |
+------------+---------+---------+-----------------------------------------------------------------------------------------------------------------+

**Note:** In the calls shown above, the source polygon is specified by the arguments with suffix ``0``. The routine copies the first ``ntv0`` connectivity entries and the coordinates of the vertices referenced by those entries. Vertex numbering is preserved, and the values of ``ntp0`` and ``ntv0`` are copied to ``ntp`` and ``ntv``. Other output array entries are not defined by the routine. Fortran and C callers must provide separate storage for the source and destination arrays.
