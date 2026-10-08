3.10 ``intc3d`` – Arithmetic mean of intersection vertices for arbitrary polyhedra
==================================================================================

The ``tintc3d`` routine computes the arithmetic mean of the intersection points generated where the polyhedron edges cross the plane :math:`\mathbf n\cdot\mathbf x+\texttt{c}=0`. The result is returned as the three-component vector ``cen`` in global coordinates.

This provides a representative point for the cut feature, useful for initializing PLIC fitting procedures.

**Fortran:**

.. code:: fortran

   call intc3d(c,cen,iecen,ipv,nipv,ntp,nts,vertp,xnc,ync,znc)

**C:**

.. code:: c

   intc3d(&c,cen,&iecen,ipv,nipv,&ntp,&nts,vertp,&xnc,&ync,&znc);

**Python:**

.. code:: python

   (cen,iecen) = voft.intc3d(c,ipv,nipv,ntp,nts,vertp,xnc,ync,znc)

**Arguments**:

+-------------------+-----------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``c``             | ``IN``    | ``W_P`` | scalar representing the signed distance from the PLIC interface to the origin along the normal vector :math:`\boldsymbol{n}`                                          |
+-------------------+-----------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``cen``           | ``OUT``   | ``W_P`` | vector representing the arithmetic mean of the intersection vertex coordinates                                                                                        |
+-------------------+-----------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``iecen``         | ``OUT``   | ``I_P`` | integer status flag: 1 if successful, 0 otherwise                                                                                                                     |
+-------------------+-----------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ipv``           | ``IN``    | ``I_P`` | array of dimensions ``(ns,nv)`` storing the vertex indices defining each face boundary                                                                                |
+-------------------+-----------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``nipv``          | ``IN``    | ``I_P`` | array of length :math:`\texttt{ns}` storing the number of vertices per face boundary                                                                                  |
+-------------------+-----------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ntp``           | ``IN``    | ``I_P`` | maximum vertex index in the connectivity list                                                                                                                         |
+-------------------+-----------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``nts``           | ``IN``    | ``I_P`` | total number of face boundaries                                                                                                                                       |
+-------------------+-----------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vertp``         | ``INOUT`` | ``W_P`` | array of dimensions :math:`({nv},3)` containing the vertex coordinates; rows beyond ``ntp`` are used to store additional intersection vertices during the calculation |
+-------------------+-----------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``xnc, ync, znc`` | ``IN``    | ``W_P`` | :math:`x,y,z`-components of the unit-length vector :math:`\boldsymbol{n}` normal to the PLIC interface pointing towards the liquid phase                              |
+-------------------+-----------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _note-4:

Note:
^^^^^

The routine preserves the original connectivity, size parameters, and vertex coordinates up to index ``ntp``, but may write intersection coordinates to subsequent rows of ``vertp``. The array must therefore have sufficient capacity and, in Python, must be writable and Fortran-contiguous.

Use ``cen`` only when ``iecen=1``. When ``iecen=0``, no intersection-point mean has been computed, and ``cen`` is set to zero.

The result is an arithmetic mean of intersection points, not an area-weighted centroid. For non-convex or disconnected sections, this point need not lie within the section.

To compute the area centroid of the planar section, use ``inte3d`` to generate the truncated geometry, identify the face boundaries created by the cut, and compute the centroid by post-processing.
