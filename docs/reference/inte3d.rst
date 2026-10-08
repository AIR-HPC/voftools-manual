3.7 ``inte3d`` – Half-space truncation of arbitrary polyhedra
=============================================================

.. _sec:inte3d:

The ``inte3d`` routine performs geometric clipping of an arbitrary polyhedron against a half-space defined by the plane :math:`\mathbf{n} \cdot \mathbf{x} + \texttt{c} = 0`. It retains the portion of the polyhedron lying on the positive side of the plane (i.e., where :math:`\mathbf{n} \cdot \mathbf{x} + \texttt{c} > 0`, consistent with the liquid phase convention) and discards the portion on the negative side.

**Fortran:**

.. code:: fortran

   call inte3d(c,icontn,icontp,ipv,nipv,ntp,nts,ntv,vertp, &
               xnc,xns,ync,yns,znc,zns)

**C:**

.. code:: c

   inte3d(&c,&icontn,&icontp,ipv,nipv,&ntp,&nts,&ntv,vertp,
   &xnc,xns,&ync,yns,&znc,zns);

**Python:**

.. code:: python

   ntp = np.array(ntp, dtype=np.int32)
   nts = np.array(nts, dtype=np.int32)
   ntv = np.array(ntv, dtype=np.int32)  
   (icontn,icontp) = voft.inte3d(c,ipv,nipv,ntp,nts,ntv,vertp,xnc,xns,ync,yns,znc,zns)

**Arguments**:

+-------------------+-----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``c``             | ``IN``    | ``W_P`` | scalar representing the signed distance from the PLIC interface to the origin along the normal vector :math:`\boldsymbol{n}`                                                    |
+-------------------+-----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``icontn``        | ``OUT``   | ``I_P`` | number of original polyhedron vertices satisfying :math:`\mathbf n\cdot\mathbf x+\texttt{c}\leq0`                                                                               |
+-------------------+-----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``icontp``        | ``OUT``   | ``I_P`` | number of original polyhedron vertices satisfying :math:`\mathbf n\cdot\mathbf x+\texttt{c}>0`                                                                                  |
+-------------------+-----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ipv``           | ``INOUT`` | ``I_P`` | array of dimensions ``(ns,nv)`` storing the vertex indices defining each face boundary; updated for the truncated geometry                                                      |
+-------------------+-----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``nipv``          | ``INOUT`` | ``I_P`` | array of length :math:`\texttt{ns}` storing the number of vertices per face boundary; updated for the truncated geometry                                                        |
+-------------------+-----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ntp``           | ``INOUT`` | ``I_P`` | maximum vertex index in the connectivity list; updated after truncation                                                                                                         |
+-------------------+-----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``nts``           | ``INOUT`` | ``I_P`` | total number of face boundaries; updated after truncation                                                                                                                       |
+-------------------+-----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ntv``           | ``INOUT`` | ``I_P`` | total number of vertices; updated after truncation                                                                                                                              |
+-------------------+-----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vertp``         | ``INOUT`` | ``W_P`` | array of dimensions :math:`({nv},3)` storing the :math:`x,y,z`-coordinates of each vertex; updated for the truncated geometry                                                   |
+-------------------+-----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``xnc, ync, znc`` | ``IN``    | ``W_P`` | :math:`x,y,z`-components of the unit-length vector :math:`\boldsymbol{n}` normal to the PLIC interface pointing towards the liquid phase                                        |
+-------------------+-----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``xns, yns, zns`` | ``INOUT`` | ``W_P`` | arrays of length :math:`\texttt{ns}` storing the :math:`x,y,z`-components of the outward-pointing unit normal vector for each face boundary; updated for the truncated geometry |
+-------------------+-----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** The geometry is updated only when both ``icontp`` and ``icontn`` are positive. If :math:`\texttt{icontn}=0`, the entire polyhedron is retained and the geometry remains unchanged. If :math:`\texttt{icontp}=0`, the retained volume is zero, but the geometry arrays and size parameters also remain unchanged. The caller must therefore check these counters before using the returned geometry.
