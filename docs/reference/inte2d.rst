3.25 ``inte2d`` – Half-space truncation of arbitrary polygons
=============================================================

The ``inte2d`` routine performs geometric clipping of an arbitrary polygon against a half-space defined by the line :math:`\mathbf{n} \cdot \mathbf{x} + \texttt{c} = 0`. It retains the portion of the polygon lying on the positive side of the line (i.e., where :math:`\mathbf{n} \cdot \mathbf{x} + \texttt{c} > 0`, consistent with the liquid phase convention) and discards the portion on the negative side.

**Fortran:**

.. code:: fortran

   call inte2d(c,icontn,icontp,ipv,ntp,ntv,vertp,xnc,ync)

**C:**

.. code:: c

   inte2d(&c,&icontn,&icontp,ipv,&ntp,&ntv,vertp,&xnc,&ync);

**Python:**

.. code:: python

   ntp = np.array(ntp, dtype=np.int32)
   ntv = np.array(ntv, dtype=np.int32)  
   (icontn, icontp) = voft.inte2d(c,ipv,ntp,ntv,vertp,xnc,ync)

**Arguments:**

+--------------+-----------+---------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``c``        | ``IN``    | ``W_P`` | scalar representing the signed distance from the PLIC interface to the origin along the unit normal vector :math:`\boldsymbol{n}`      |
+--------------+-----------+---------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``icontn``   | ``OUT``   | ``I_P`` | number of original polygon vertices satisfying :math:`\boldsymbol{n} \cdot \boldsymbol{x} + \texttt{c} \le 0`                          |
+--------------+-----------+---------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``icontp``   | ``OUT``   | ``I_P`` | number of original polygon vertices satisfying :math:`\boldsymbol{n} \cdot \boldsymbol{x} + \texttt{c} > 0`                            |
+--------------+-----------+---------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``ipv``      | ``INOUT`` | ``I_P`` | array of length :math:`\texttt{nv}` storing the vertex indices defining the polygon; updated for the truncated geometry                |
+--------------+-----------+---------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``ntp``      | ``INOUT`` | ``I_P`` | maximum vertex index in the connectivity list; updated after truncation                                                                |
+--------------+-----------+---------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``ntv``      | ``INOUT`` | ``I_P`` | total number of vertices; updated after truncation                                                                                     |
+--------------+-----------+---------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``vertp``    | ``INOUT`` | ``W_P`` | array of dimensions :math:`({nv},2)` storing the :math:`x,y`-coordinates of each vertex; updated for the truncated geometry            |
+--------------+-----------+---------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``xnc, ync`` | ``IN``    | ``W_P`` | :math:`x,y`-components of the unit-length vector :math:`\boldsymbol{n}` normal to the PLIC interface pointing towards the liquid phase |
+--------------+-----------+---------+----------------------------------------------------------------------------------------------------------------------------------------+

.. _note-5:

Note:
^^^^^

The routine modifies ``ipv``, ``vertp``, ``ntp``, and ``ntv`` in place only when both ``icontn`` and ``icontp`` are positive. If :math:`\texttt{icontn} = 0`, the entire polygon is retained and the input geometry remains unchanged. If :math:`\texttt{icontp} = 0`, the retained region is empty, but the input geometry also remains unchanged; the caller must handle this case explicitly. To preserve the original geometry when truncation occurs, make a copy before calling the routine, for example using ``cppol2d``.
