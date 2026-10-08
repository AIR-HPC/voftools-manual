3.26 ``toolv2d`` – Area computation for arbitrary polygons
==========================================================

The ``toolv2d`` routine computes the signed area of an arbitrary polygon (convex or non-convex) defined by its vertices.

**Fortran:**

.. code:: fortran

   call toolv2d(ipv,ntv,vertp,vol)

**C:**

.. code:: c

   toolv2d(ipv,&ntv,vertp,&vol);

**Python:**

.. code:: python

   vol = voft.toolv2d(ipv,ntv,vertp)

**Arguments:**

+-----------+---------+---------+-----------------------------------------------------------------------------------------+
| ``ipv``   | ``IN``  | ``I_P`` | array of length :math:`\texttt{nv}` storing the vertex indices defining the polygon     |
+-----------+---------+---------+-----------------------------------------------------------------------------------------+
| ``ntv``   | ``IN``  | ``I_P`` | total number of vertices                                                                |
+-----------+---------+---------+-----------------------------------------------------------------------------------------+
| ``vertp`` | ``IN``  | ``W_P`` | array of dimensions :math:`({nv},2)` storing the :math:`x,y`-coordinates of each vertex |
+-----------+---------+---------+-----------------------------------------------------------------------------------------+
| ``vol``   | ``OUT`` | ``W_P`` | scalar representing the signed area of the polygon                                      |
+-----------+---------+---------+-----------------------------------------------------------------------------------------+

**Note:** The boundary traversal is defined by the first ``ntv`` entries of ``ipv``. For a simple polygon, counterclockwise ordering gives a positive area and clockwise ordering gives a negative area. Reversing the traversal reverses the sign. For self-intersecting boundaries, the result is an algebraic signed area, which need not equal the geometric area of the enclosed regions. The routine preserves the sign, which may be meaningful in fluid-transport calculations according to the adopted orientation convention.
