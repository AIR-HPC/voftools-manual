3.18 ``dist3d`` – Point-to-convex-polygon Distance in 3D
========================================================

The ``dist3d`` routine computes the shortest Euclidean distance from a point :math:`P` in 3D space to a planar convex polygon defined by its vertex coordinates. The calculation accounts for whether the orthogonal projection of :math:`P` onto the polygon’s plane lies within or outside the polygon’s boundary. If the projection is inside, the distance is the perpendicular distance to the plane; otherwise, it is the minimum distance to the polygon’s edges or vertices.

**Fortran:**

.. code:: fortran

   call dist3d(d,n,x,y,z,xp,yp,zp)

**C:**

.. code:: c

   dist3d(&d,&n,x,y,z,&xp,&yp,&zp);

**Python:**

.. code:: python

   d = voft.dist3d(n,x,y,z,xp,yp,zp)

**Arguments:**

+----------------+---------+---------+-----------------------------------------------------------------------------------------+
| ``d``          | ``OUT`` | ``W_P`` | scalar representing the shortest Euclidean distance from point :math:`P` to the polygon |
+----------------+---------+---------+-----------------------------------------------------------------------------------------+
| ``n``          | ``IN``  | ``I_P`` | scalar representing the number of vertices defining the polygon                         |
+----------------+---------+---------+-----------------------------------------------------------------------------------------+
| ``x, y, z``    | ``IN``  | ``W_P`` | arrays of length ``nv`` storing the coordinates of the polygon vertices                 |
+----------------+---------+---------+-----------------------------------------------------------------------------------------+
| ``xp, yp, zp`` | ``IN``  | ``W_P`` | scalars storing the coordinates of point :math:`P`                                      |
+----------------+---------+---------+-----------------------------------------------------------------------------------------+

**Note:** The polygon must be planar, convex, and non-degenerate, with :math:`3 \leq \texttt{n} \leq \texttt{nv}`. Its vertices must be supplied consecutively along the boundary, either clockwise or counterclockwise, without repeating the first vertex at the end. Only the first ``n`` entries of ``x``, ``y``, and ``z`` are used. The returned distance is non-negative.
