3.14 ``box3d`` – Bounding box computation for point sets
========================================================

The ``box3d`` routine computes the bounding box of a given set of points, defined as the smallest axis-aligned rectangular parallelepiped containing all points. It returns the minimum and maximum coordinates along each axis (:math:`x, y, z`).

**Fortran:**

.. code:: fortran

   call box3d(box,ntp,vertp)

**C:**

.. code:: c

   box3d(box,&ntp,vertp);

**Python:**

.. code:: python

   box = voft.box3d(ntp,vertp)

**Arguments:**

+-----------+---------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``box``   | ``OUT`` | ``W_P`` | array of length :math:`(6)` storing the bounding box coordinates. Indices are mapped as follows: :math:`[x_\mathrm{min}, x_\mathrm{max}, y_\mathrm{min}, y_\mathrm{max}, z_\mathrm{min}, z_\mathrm{max}]` |
+-----------+---------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ntp``   | ``IN``  | ``I_P`` | total number of points in the set                                                                                                                                                                         |
+-----------+---------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vertp`` | ``IN``  | ``W_P`` | array of dimensions :math:`({nv},3)` storing the :math:`x,y,z`-coordinates of each point                                                                                                                  |
+-----------+---------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** The routine processes the first ``ntp`` rows of ``vertp``, with :math:`1\leq \texttt{ntp}\leq \texttt{nv}`. It does not use connectivity information to identify active vertices. Consequently, unused vertices within this range are also included in the bounding-box calculation.
