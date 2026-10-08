3.19 ``initf3d`` – Volume fraction initialization via Cartesian shadow grid
===========================================================================

.. _sec:initf3d:

The ``initf3d`` computes the volume fraction ``vf`` of a material body within an arbitrary polyhedral cell. The boundary of the material body is defined by a user-provided implicit function :math:`\phi(x,y,z) \equiv \texttt{func3d}(x,y,z)`, with the material occupying the region :math:`\phi(x,y,z)>0`.

To approximate non-planar interfaces, the volume integral is evaluated using a composite numerical rule over a uniform Cartesian grid (shadow grid) superimposed on the polyhedral cell. This grid consists of :math:`\texttt{nc} \times \texttt{nc} \times \texttt{nc}` sub-cells, where :math:`\texttt{nc}` is the resolution parameter. The integration scheme follows the methodology detailed in Refs. [\ :ref:`7 <bib-lopez13>`\ , \ :ref:`10 <bib-lopez18jcp>`\ ].

**Fortran:**

.. code:: fortran

   call initf3d(func3d,ipv,nc,nipv,ntp,nts,ntv,tol,vertp,vf, &
         xns,yns,zns)

**C:**

.. code:: c

   initf3d(func3d,ipv,&nc,nipv,&ntp,&nts,&ntv,&tol,vertp,&vf,
   xns,yns,zns);

**Python:**

.. code:: python

   vf = voft.initf3d(func3d,ipv,nc,nipv,ntp,nts,ntv,tol,vertp,xns,yns,zns)

**Arguments:**

+-------------------+---------------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``func3d``        | ``VOFTOOLS_FUNC3D`` | ``PROCEDURE`` | external procedure. User-defined implicit function defining the material interface. The routine samples this function to determine if points lie inside or outside the material                                                                                                                              |
+-------------------+---------------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ipv``           | ``IN``              | ``I_P``       | array of dimensions ``(ns,nv)`` storing the vertex indices defining each face boundary of the polyhedron                                                                                                                                                                                                     |
+-------------------+---------------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``nc``            | ``IN``              | ``I_P``       | scalar specifying the number of sub-cells along each coordinate axis of the superimposed Cartesian grid used for the refinement process in the numerical integration                                                                                                                                         |
+-------------------+---------------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``nipv``          | ``IN``              | ``I_P``       | array of length :math:`\texttt{ns}` storing the number of vertices per face boundary                                                                                                                                                                                                                         |
+-------------------+---------------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ntp``           | ``IN``              | ``I_P``       | maximum vertex index in the connectivity list                                                                                                                                                                                                                                                                |
+-------------------+---------------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``nts``           | ``IN``              | ``I_P``       | total number of face boundaries of the polyhedron                                                                                                                                                                                                                                                            |
+-------------------+---------------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ntv``           | ``IN``              | ``I_P``       | total number of vertices in the polyhedron                                                                                                                                                                                                                                                                   |
+-------------------+---------------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``tol``           | ``IN``              | ``W_P``       | positive threshold parameter used in the preliminary vertex-based classification. Cartesian subdivision is performed when the vertex signs differ or when the minimum absolute value of ``func3d`` at the vertices is smaller than ``tol*(xmax-xmin)``. This parameter is not an integration-error tolerance |
+-------------------+---------------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vertp``         | ``IN``              | ``W_P``       | array of dimensions :math:`({nv},3)` storing the :math:`x,y,z`-coordinates of each vertex                                                                                                                                                                                                                    |
+-------------------+---------------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vf``            | ``OUT``             | ``W_P``       | scalar representing the computed volume fraction of the material within the polyhedral cell. Value lies in :math:`[0,1]`                                                                                                                                                                                     |
+-------------------+---------------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``xns, yns, zns`` | ``IN``              | ``W_P``       | arrays of length :math:`\texttt{ns}` storing the :math:`x,y,z`-components of the outward-pointing unit normal vector for each face boundary                                                                                                                                                                  |
+-------------------+---------------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** Interfaces enclosed within the cell may be missed by the preliminary vertex-based classification. Increasing ``nc`` does not affect this classification. During subdivision, features that are not resolved by the subcell vertex samples may also remain undetected. The subdivision parameter ``nc`` must be a positive integer.
