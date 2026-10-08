3.8 ``toolv3d`` – Volume computation for arbitrary polyhedra
============================================================

The ``toolv3d`` routine computes the volume of an arbitrary polyhedron.

**Fortran:**

.. code:: fortran

   call toolv3d(ipv,nipv,nts,vertp,vol,xns,yns,zns)

**C:**

.. code:: c

   toolv3d(ipv,nipv,&nts,vertp,&vol,xns,yns,zns);

**Python:**

.. code:: python

   vol = voft.toolv3d(ipv,nipv,nts,vertp,xns,yns,zns)

**Arguments:**

+-------------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``ipv``           | ``IN``  | ``I_P`` | array of dimensions ``(ns,nv)`` storing the vertex indices defining each face boundary                                                      |
+-------------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``nipv``          | ``IN``  | ``I_P`` | array of length :math:`\texttt{ns}` storing the number of vertices per face boundary                                                        |
+-------------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``nts``           | ``IN``  | ``I_P`` | total number of face boundaries                                                                                                             |
+-------------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``vertp``         | ``IN``  | ``W_P`` | array of dimensions :math:`({nv},3)` storing the :math:`x,y,z`-coordinates of each vertex                                                   |
+-------------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``vol``           | ``OUT`` | ``W_P`` | scalar representing the signed volume of the polyhedron                                                                                     |
+-------------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``xns, yns, zns`` | ``IN``  | ``W_P`` | arrays of length :math:`\texttt{ns}` storing the :math:`x,y,z`-components of the outward-pointing unit normal vector for each face boundary |
+-------------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** The routine computes an algebraic volume whose sign depends on the orientation of the face boundaries. Negative values are preserved and may be meaningful, for example when oriented donating polyhedra are used to represent fluid transport across cell faces. In such applications, the sign distinguishes inflow from outflow according to the adopted orientation convention.
