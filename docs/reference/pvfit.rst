3.15 ``pvfit`` – Paraboloid fitting for polyhedral interface reconstruction
===========================================================================

The ``pvfit`` routine fits a paraboloid to a set of :math:`\texttt{npol}` polygons by constructing volumetric columns aligned with a local reference system (:math:`\texttt{u},\texttt{v},\texttt{f}`). The interface of this paraboloid, defined within the local reference system, is given by Eq. (\ :ref:`3.1 <eq:parab>`\ ), where the coefficient vector is :math:`\texttt{coef}=[c_1,c_2,c_3,c_4,c_5,c_6]`. Specifically, the routine projects the discrete polygons onto the local reference plane—defined by the orthonormal basis :math:`\texttt{vn0}` and reference point :math:`\texttt{vp0}`—thereby forming vertical columns bounded by the projected polygon edges. It then determines the paraboloid that best approximates the volume of these columns using a least-squares technique [\ :ref:`4 <bib-jibben19>`\ , \ :ref:`14 <bib-lopez26>`\ ].

**Fortran:**

.. code:: fortran

   call pvfit(coef,errfit,niv,npol,vn0,vp0,xn,xv,yn,yv,zn,zv)

**C:**

.. code:: c

   pvfit(coef,&errfit,niv,&npol,vn0,vp0,xn,xv,yn,yv,zn,zv);

**Python:**

.. code:: python

   (coef,errfit) = voft.pvfit(niv,npol,vn0,vp0,xn,xv,yn,yv,zn,zv)

**Arguments:**

+------------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``coef``               | ``OUT`` | ``W_P`` | array of length :math:`(6)` storing the coefficients :math:`[c_1,c_2,c_3,c_4,c_5,c_6]` of the fitted paraboloid in the local orthonormal basis                   |
+------------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``errfit``             | ``OUT`` | ``W_P`` | scalar representing the sum of squared volumetric residuals over the input polygons, evaluated using the fitted coefficients; this quantity is not normalized    |
+------------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``niv``                | ``IN``  | ``I_P`` | array of length (``ns``) storing the number of vertices of each polygon                                                                                          |
+------------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``npol``               | ``IN``  | ``I_P`` | total number of polygons                                                                                                                                         |
+------------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vn0``                | ``IN``  | ``W_P`` | array of dimensions :math:`(3,3)` whose rows contain the unit vectors of the local ``f``-, ``u``-, and ``v``-axes, respectively, expressed in global coordinates |
+------------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vp0``                | ``IN``  | ``W_P`` | array of length :math:`(3)` storing the origin of the local reference system in global coordinates                                                               |
+------------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``xn``, ``yn``, ``zn`` | ``IN``  | ``W_P`` | arrays of length (``ns``) storing :math:`(x,y,z)`-components of the unit-length normal vectors for each polygon                                                  |
+------------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``xv``, ``yv``, ``zv`` | ``IN``  | ``W_P`` | arrays of dimensions (:math:`\texttt{ns},\texttt{nv}`) storing the :math:`(x,y,z)`-coordinates of every vertex of each polygon                                   |
+------------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** The polygon set must provide at least six independent volumetric constraints for the six fitted coefficients. The normal of each polygon must have a nonzero component along the local ``f``-axis. Having six or more polygons alone does not guarantee a nonsingular fitting system.
