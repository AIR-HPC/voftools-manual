3.17 ``cppol3d`` – Polyhedron deep copy
=======================================

The ``cppol3d`` routine creates a deep copy of a polyhedron’s geometric and topological structure. It duplicates the connectivity information, vertex coordinates, face normals, and plane distances, ensuring that the new polyhedron is an independent data structure from the original.

**Fortran:**

.. code:: fortran

   call cppol3d(cs,cs0,ipv,ipv0,nipv,nipv0,ntp,ntp0,nts,nts0, &
         ntv,ntv0,vertp,vertp0,xns,xns0,yns,yns0,zns,zns0)

**C:**

.. code:: c

   cppol3d(cs,cs0,ipv,ipv0,nipv,nipv0,&ntp,&ntp0,&nts,&nts0,
   &ntv,&ntv0,vertp,vertp0,xns,xns0,yns,yns0,zns,zns0);

**Python:**

.. code:: python

   (cs,ipv,nipv,ntp,nts,ntv,vertp,xns,yns,zns) = voft.cppol3d(cs0,ipv0,nipv0,ntp0,nts0,ntv0,vertp0,xns0,yns0,zns0)

**Arguments:**

+----------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``cs``               | ``OUT`` | ``W_P`` | array of length ``ns`` storing the signed distance from the plane containing each face boundary of the copied polyhedron to the origin, along the outward-pointing normal vector   |
+----------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``cs0``              | ``IN``  | ``W_P`` | array of length ``ns`` storing the signed distance from the plane containing each face boundary of the original polyhedron to the origin, along the outward-pointing normal vector |
+----------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ipv``              | ``OUT`` | ``I_P`` | array of dimensions ``(ns,nv)`` storing the vertex indices defining the boundary of each face for the copied polyhedron                                                            |
+----------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ipv0``             | ``IN``  | ``I_P`` | array of dimensions ``(ns,nv)`` storing the vertex indices defining the boundary of each face for the original polyhedron                                                          |
+----------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``nipv``             | ``OUT`` | ``I_P`` | array of length :math:`\texttt{ns}` storing the number of vertices per face boundary for the copied polyhedron                                                                     |
+----------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``nipv0``            | ``IN``  | ``I_P`` | array of length :math:`\texttt{ns}` storing the number of vertices per face boundary for the original polyhedron                                                                   |
+----------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ntp``              | ``OUT`` | ``I_P`` | maximum vertex index in the connectivity list of the copied polyhedron                                                                                                             |
+----------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ntp0``             | ``IN``  | ``I_P`` | maximum vertex index in the connectivity list of the original polyhedron                                                                                                           |
+----------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``nts``              | ``OUT`` | ``I_P`` | total number of face boundaries of the copied polyhedron                                                                                                                           |
+----------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``nts0``             | ``IN``  | ``I_P`` | total number of face boundaries of the original polyhedron                                                                                                                         |
+----------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ntv``              | ``OUT`` | ``I_P`` | total number of vertices in the copied polyhedron                                                                                                                                  |
+----------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ntv0``             | ``IN``  | ``I_P`` | total number of vertices in the original polyhedron                                                                                                                                |
+----------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vertp``            | ``OUT`` | ``W_P`` | array of dimensions :math:`({nv},3)` storing the :math:`x,y,z`-coordinates of each vertex of the copied polyhedron                                                                 |
+----------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vertp0``           | ``IN``  | ``W_P`` | array of dimensions :math:`({nv},3)` storing the :math:`x,y,z`-coordinates of each vertex of the original polyhedron                                                               |
+----------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``xns, yns, zns``    | ``OUT`` | ``W_P`` | arrays of length :math:`\texttt{ns}` storing the :math:`x,y,z`-components of the outward-pointing unit normal vector for each face of the copied polyhedron                        |
+----------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``xns0, yns0, zns0`` | ``IN``  | ``W_P`` | arrays of length :math:`\texttt{ns}` storing the :math:`x,y,z`-components of the outward-pointing unit normal vector for each face of the original polyhedron                      |
+----------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** The source polyhedron is specified by the arguments with suffix ``0``. The routine copies the vertex coordinates up to ``ntp0``, the face data up to ``nts0``, and the connectivity entries up to ``nipv0(i)`` for each face. Entries outside these ranges are not defined by the routine. The plane constants ``cs0`` are copied without recomputation. Fortran and C callers must provide separate storage for the source and destination arrays.
