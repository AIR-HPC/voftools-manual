3.28 ``dist2d`` – Point-to-segment distance
===========================================

.. _sec:dist2d:

The ``dist2d`` routine computes the shortest Euclidean distance from a point :math:`P` with coordinates (``xp``,\ ``yp``) to the segment with endpoints (``x(1),y(1)``) and (``x(2),y(2)``). If the orthogonal projection of :math:`P` onto the supporting line lies within the segment, the routine returns the perpendicular distance to that line; otherwise, it returns the distance to the nearest endpoint.

**Fortran:**

.. code:: fortran

   call dist2d(d,x,y,xp,yp)

**C:**

.. code:: c

   dist2d(&d,x,y,&xp,&yp);

**Python:**

.. code:: python

   d = voft.dist2d(x,y,xp,yp)

**Arguments:**

+------------+---------+---------+-----------------------------------------------------------------------------------------+
| ``d``      | ``OUT`` | ``W_P`` | scalar representing the shortest Euclidean distance from point :math:`P` to the segment |
+------------+---------+---------+-----------------------------------------------------------------------------------------+
| ``x, y``   | ``IN``  | ``W_P`` | arrays of length :math:`2` storing the coordinates of the segment vertices              |
+------------+---------+---------+-----------------------------------------------------------------------------------------+
| ``xp, yp`` | ``IN``  | ``W_P`` | scalars storing the coordinates of point :math:`P`                                      |
+------------+---------+---------+-----------------------------------------------------------------------------------------+

**Note:** The segment endpoints must be distinct. The returned distance is non-negative and does not depend on the ordering of the endpoints. The routine does not explicitly handle zero-length segments.
