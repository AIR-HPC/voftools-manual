3.12 ``areaface`` – Area of arbitrary planar polygons
=====================================================

The ``areaface`` routine computes the area of an arbitrary oriented planar polygon (either convex or non-convex). This routine is particularly useful for unsplit advection schemes based on the WATIA methodology, where face areas are required for flux calculations.

:math:`\,`

**Fortran:**

.. code:: fortran

   call areaface(a,ipv,ntv,vertp,xns,yns,zns)

**C:**

.. code:: c

   areaface(&a,ipv,&ntv,vertp,&xns,&yns,&zns);

**Python:**

.. code:: python

   a = voft.areaface(ipv,ntv,vertp,xns,yns,zns)

**Arguments:**

+-------------------+---------+---------+-------------------------------------------------------------------------------------------+
| ``a``             | ``OUT`` | ``W_P`` | scalar representing the signed area of the arbitrary oriented planar polygon              |
+-------------------+---------+---------+-------------------------------------------------------------------------------------------+
| ``ipv``           | ``IN``  | ``I_P`` | array of length :math:`(nv)` storing the vertex indices defining the polygon perimeter    |
+-------------------+---------+---------+-------------------------------------------------------------------------------------------+
| ``ntv``           | ``IN``  | ``I_P`` | total number of vertices                                                                  |
+-------------------+---------+---------+-------------------------------------------------------------------------------------------+
| ``vertp``         | ``IN``  | ``W_P`` | array of dimensions :math:`({nv},3)` storing the :math:`x,y,z`-coordinates of each vertex |
+-------------------+---------+---------+-------------------------------------------------------------------------------------------+
| ``xns, yns, zns`` | ``IN``  | ``W_P`` | :math:`x,y,z`-components of the unit normal vector to the polygon plane                   |
+-------------------+---------+---------+-------------------------------------------------------------------------------------------+

**Note:** The sign of ``a`` is determined by the vertex ordering relative to the supplied unit normal. Reversing either the vertex ordering or the normal direction reverses the sign; reversing both preserves it. The routine does not normalize the supplied normal vector. Signed areas may be used in fluid-flux calculations across cell faces. Their interpretation must be consistent with the velocity direction and the adopted face-orientation convention.
