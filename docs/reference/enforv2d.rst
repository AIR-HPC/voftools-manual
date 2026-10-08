3.23 ``enforv2d`` – PLIC interface location for 2D polygons
===========================================================

The ``enforv2d`` routine solves the two-dimensional VCE problem to locate the PLIC interface within a polygonal cell. Given a target liquid area :math:`\texttt{v}`, it determines the position of the interface line such that the area of the liquid region within the cell matches the specified value.

The interface is defined by the equation :math:`\mathbf{n} \cdot \mathbf{x} + \texttt{c}=0`, where :math:`\mathbf{n} = (\texttt{xnc}, \texttt{ync})` is the unit normal vector pointing towards the liquid phase, and :math:`\texttt{c}` is a scalar parameter determining the interface position. The routine computes :math:`\texttt{c}` such that:

.. math:: \mbox{Area}(\{\boldsymbol{x} \in \Omega_\text{cell} | \boldsymbol{n} \cdot \boldsymbol{x} +  \texttt{c} > 0 \}) = \texttt{v}

where :math:`\Omega_{\text{cell}}` is the domain of the polygonal cell.

:math:`\,`

**Fortran:**

.. code:: fortran

   call enforv2d(c,ipv,ntp,ntv,v,vt,vertp,xnc,ync)

**C:**

.. code:: c

   enforv2d(&c,ipv,&ntp,&ntv,&v,&vt,vertp,&xnc,&ync);

**Python:**

.. code:: python

   c = voft.enforv2d(ipv,ntp,ntv,v,vt,vertp,xnc,ync)

**Arguments:**

+--------------+---------+---------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``c``        | ``OUT`` | ``W_P`` | scalar representing the signed distance from the PLIC interface to the origin along the unit normal vector :math:`\boldsymbol{n}`      |
+--------------+---------+---------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``ipv``      | ``IN``  | ``I_P`` | array of length :math:`\texttt{nv}` storing the vertex indices defining the polygon                                                    |
+--------------+---------+---------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``ntp``      | ``IN``  | ``I_P`` | maximum vertex index in the connectivity list                                                                                          |
+--------------+---------+---------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``ntv``      | ``IN``  | ``I_P`` | total number of vertices                                                                                                               |
+--------------+---------+---------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``v``        | ``IN``  | ``W_P`` | scalar representing the target liquid area within the cell                                                                             |
+--------------+---------+---------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``vt``       | ``IN``  | ``W_P`` | scalar representing the total area of the polygon                                                                                      |
+--------------+---------+---------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``vertp``    | ``IN``  | ``W_P`` | array of dimensions :math:`({nv},2)` storing the :math:`x,y`-coordinates of each vertex                                                |
+--------------+---------+---------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``xnc, ync`` | ``IN``  | ``W_P`` | :math:`x,y`-components of the unit-length vector :math:`\boldsymbol{n}` normal to the PLIC interface pointing towards the liquid phase |
+--------------+---------+---------+----------------------------------------------------------------------------------------------------------------------------------------+

**Note:** This routine serves as the general solver for arbitrary 2D polygons. For axis-aligned rectangular cells, the more efficient analytical method in ``enforv2dsz`` should be preferred. The input polygon must have compact vertex numbering, with :math:`\texttt{ntp} = \texttt{ntv}`. The total cell area ``vt`` must be positive, and the prescribed liquid area must satisfy :math:`0 \le \texttt{v} \le \texttt{vt}`. The argument ``v`` is an area, not an area fraction; for a prescribed fraction :math:`\alpha`, use :math:`\texttt{v} = \alpha \texttt{vt}`. The input polygon is not modified.
