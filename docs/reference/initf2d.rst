3.29 ``initf2d`` – Area fraction initialization for 2D geometries via Cartesian shadow grid
===========================================================================================

.. _sec:initf2d:

The ``initf2d`` routine computes the fraction of the material area contained in a 2D cell. The boundary of the material is defined by a user-provided implicit function :math:`\phi(x, y) \equiv \texttt{func2d}(x, y)`, with the material occupying the region :math:`\phi(x, y) > 0`.

To approximate curved interfaces, the routine subdivides the cell’s bounding box into a uniform Cartesian shadow grid with :math:`\texttt{nc} \times \texttt{nc}` subcells. Within each intersected subcell, interface intersections are estimated by linear interpolation of the sampled implicit-function values. The resulting material areas are accumulated and divided by the total cell area. Accuracy depends on the grid resolution and the interface geometry.

**Fortran:**

.. code:: fortran

   call initf2d(func2d,ipv,nc,ntp,ntv,tol,vertp,vf)

**C:**

.. code:: c

   initf2d(func2d,ipv,&nc,&ntp,&ntv,&tol,vertp,&vf);

**Python:**

.. code:: python

   vf = voft.initf2d(func2d,ipv,nc,ntp,ntv,tol,vertp)

**Arguments:**

+------------+---------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``func2d`` | ``VOFTOOLS_FUNC2D`` | ``PROCEDURE`` | external procedure. User-defined implicit function defining the material interface. The routine samples this function to determine if points lie inside or outside the material                                                                                                                                                             |
+------------+---------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ipv``    | ``IN``              | ``I_P``       | array of length ``nv`` storing the vertex indices defining the polygon                                                                                                                                                                                                                                                                      |
+------------+---------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``nc``     | ``IN``              | ``I_P``       | scalar specifying the number of sub-cells along each coordinate axis of the superimposed Cartesian grid used for the refinement process in the numerical integration                                                                                                                                                                        |
+------------+---------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ntp``    | ``IN``              | ``I_P``       | maximum vertex index in the connectivity list                                                                                                                                                                                                                                                                                               |
+------------+---------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ntv``    | ``IN``              | ``I_P``       | total number of vertices in the polygon                                                                                                                                                                                                                                                                                                     |
+------------+---------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``tol``    | ``IN``              | ``W_P``       | positive threshold parameter used in the preliminary vertex-based classification. Cartesian subdivision is performed when the vertex signs differ or when the minimum absolute value of ``func2d`` at the vertices is smaller than :math:`\texttt{tol}*(\texttt{xmax}-\texttt{xmin})`. This parameter is not an integration-error tolerance |
+------------+---------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vertp``  | ``IN``              | ``W_P``       | array of dimensions :math:`({nv},2)` storing the :math:`x,y`-coordinates of each vertex                                                                                                                                                                                                                                                     |
+------------+---------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vf``     | ``OUT``             | ``W_P``       | scalar representing the computed area fraction of the material within the polygonal cell. Value lies in :math:`[0,1]`                                                                                                                                                                                                                       |
+------------+---------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** Interfaces enclosed within the cell may be missed by the preliminary vertex-based classification. Increasing ``nc`` does not affect this classification. During subdivision, features that are not resolved by the subcell vertex samples may also remain undetected. The subdivision parameter ``nc`` must be a positive integer.
