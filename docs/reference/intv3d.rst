3.9 ``intv3d`` – Half-space integration volume for arbitrary polyhedra
======================================================================

The ``intv3d`` routine computes the signed volume of the portion of a polyhedron lying in the half-space :math:`\mathbf n\cdot\mathbf x+\texttt{c}>0`. This corresponds to the liquid-side convention used by ``inte3d``. The sign of the volume follows the boundary orientation convention described for ``toolv3d``.

**Fortran:**

.. code:: fortran

   call intv3d(c,ipv,nipv,ntp,nts,vertp,vol,xnc,xns, &
       ync,yns,znc,zns)

**C:**

.. code:: c

   intv3d(&c,ipv,nipv,&ntp,&nts,vertp,&vol,&xnc,xns,
   &ync,yns,&znc,zns);

**Python:**

.. code:: python

   vol = voft.intv3d(c,ipv,nipv,ntp,nts,vertp,xnc,xns,ync,yns,znc,zns)

**Arguments:**

+-------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``c``             | ``IN``    | ``W_P`` | scalar representing the signed distance from the PLIC interface to the origin along the normal vector :math:`\boldsymbol{n}`                                                 |
+-------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ipv``           | ``IN``    | ``I_P`` | array of dimensions ``(ns,nv)`` storing the vertex indices defining each face boundary                                                                                       |
+-------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``nipv``          | ``IN``    | ``I_P`` | array of length :math:`\texttt{ns}` storing the number of vertices per face boundary                                                                                         |
+-------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ntp``           | ``IN``    | ``I_P`` | maximum vertex index in the connectivity list                                                                                                                                |
+-------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``nts``           | ``IN``    | ``I_P`` | total number of face boundaries                                                                                                                                              |
+-------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vertp``         | ``INOUT`` | ``W_P`` | array of dimensions :math:`(\texttt{nv},3)` containing the vertex coordinates; rows beyond ``ntp`` are used to store additional intersection vertices during the calculation |
+-------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vol``           | ``OUT``   | ``W_P`` | scalar representing the signed volume of the portion of the polyhedron lying within the half-space (liquid volume)                                                           |
+-------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``xnc, ync, znc`` | ``IN``    | ``W_P`` | :math:`x,y,z`-components of the unit-length vector :math:`\boldsymbol{n}` normal to the PLIC interface pointing towards the liquid phase                                     |
+-------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``xns, yns, zns`` | ``IN``    | ``W_P`` | arrays of length :math:`\texttt{ns}` storing the :math:`x,y,z`-components of the outward-pointing unit normal vector for each face boundary                                  |
+-------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _note-3:

Note:
^^^^^

Unlike ``inte3d``, this routine does not return a complete representation of the truncated geometry. The original connectivity, size parameters, face normals, and vertex coordinates up to index ``ntp`` remain unchanged. However, additional intersection coordinates may be written to ``vertp`` beyond ``ntp``, so the array must have sufficient capacity. In Python, ``vertp`` must be a writable, Fortran-contiguous ``NumPy`` array of the required data type.
