3.11 ``inte3dface`` – Half-space intersection for planar polygons
=================================================================

The ``inte3dface`` routine computes the intersection between an arbitrary oriented planar polygon (which can be either convex or non-convex) and a half-space. This routine is particularly useful in unsplit advection schemes based on the WATIA me­tho­do­lo­gy, where accurate calculation of face intersections is critical. The retained region corresponds to the half-space :math:`\mathbf n\cdot\mathbf x+\texttt{c}>0`.

:math:`\,`

**Fortran:**

.. code:: fortran

   call inte3dface(c,icontn,icontp,ipv,ntp,ntv,vertp,xnc,ync,znc)

**C:**

.. code:: c

   inte3dface(&c,&icontn,&icontp,ipv,&ntp,&ntv,vertp,&xnc,&ync,&znc);

**Python:**

.. code:: python

   ntp = np.array(ntp, dtype=np.int32)
   ntv = np.array(ntv, dtype=np.int32)  
   (icontn,icontp) = voft.inte3dface(c,ipv,ntp,ntv,vertp,xnc,ync,znc)

**Arguments:**

+-------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``c``             | ``IN``    | ``W_P`` | scalar representing the signed distance from the PLIC interface to the origin along the normal vector :math:`\boldsymbol{n}`             |
+-------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``icontn``        | ``OUT``   | ``I_P`` | number of original polygon vertices satisfying :math:`\mathbf n\cdot\mathbf x+\texttt{c}\leq0`                                           |
+-------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``icontp``        | ``OUT``   | ``I_P`` | number of original polygon vertices satisfying :math:`\mathbf n\cdot\mathbf x+\texttt{c}>0`                                              |
+-------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``ipv``           | ``INOUT`` | ``I_P`` | array of length ``(nv)`` storing the vertex indices defining the arbitrary oriented planar polygon; updated for the truncated geometry   |
+-------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``ntp``           | ``INOUT`` | ``I_P`` | maximum vertex index in the connectivity list; updated after truncation                                                                  |
+-------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``ntv``           | ``INOUT`` | ``I_P`` | total number of vertices; updated after truncation                                                                                       |
+-------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``vertp``         | ``INOUT`` | ``W_P`` | array of dimensions :math:`({nv},3)` storing the :math:`x,y,z`-coordinates of each vertex; updated for the truncated geometry            |
+-------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``xnc, ync, znc`` | ``IN``    | ``W_P`` | :math:`x,y,z`-components of the unit-length vector :math:`\boldsymbol{n}` normal to the PLIC interface pointing towards the liquid phase |
+-------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** The geometry is updated only when both ``icontp`` and ``icontn`` are positive. If :math:`\texttt{icontn}=0`, the entire polygon is retained and the geometry remains unchanged. If :math:`\texttt{icontp}=0`, the retained area is zero, but the geometry arrays and size parameters also remain unchanged. The caller must therefore check these counters before computing the retained area or exporting the resulting geometry.
