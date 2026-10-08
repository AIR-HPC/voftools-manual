3.4 ``enforv3d`` – PLIC interface location for arbitrary polyhedra
==================================================================

The ``enforv3d`` routine addresses the VCE problem in 3D, specifically aiming to locate the PLIC interface within a polyhedral cell. The subroutine can be invoked in Fortran, C, and Python as follows:

**Fortran:**

.. code:: fortran

   call enforv3d(c,ipv,nipv,ntp,nts,ntv,v,vt,vertp,xnc,xns, & 
                 ync,yns,znc,zns) 

**C:**

.. code:: c

   enforv3d(&c,ipv,nipv,&ntp,&nts,&ntv,&v,&vt,vertp,&xnc,xns,
   &ync,yns,&znc,zns);

**Python:**

.. code:: python

   c = voft.enforv3d(ipv,nipv,ntp,nts,ntv,v,vt,vertp,xnc,xns,
   ync,yns,znc,zns)

**Arguments:**

+-------------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``c``             | ``OUT`` | ``W_P`` | scalar representing the signed distance from the PLIC interface to the origin along the normal vector :math:`\boldsymbol{n}`                |
+-------------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``ipv``           | ``IN``  | ``I_P`` | array of dimensions ``(ns,nv)`` storing the vertex indices defining each face boundary                                                      |
+-------------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``nipv``          | ``IN``  | ``I_P`` | array of length :math:`\texttt{ns}` storing the number of vertices per face boundary                                                        |
+-------------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``ntp``           | ``IN``  | ``I_P`` | maximum vertex index in the connectivity list                                                                                               |
+-------------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``nts``           | ``IN``  | ``I_P`` | total number of face boundaries                                                                                                             |
+-------------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``ntv``           | ``IN``  | ``I_P`` | total number of vertices                                                                                                                    |
+-------------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``v``             | ``IN``  | ``W_P`` | scalar representing the target liquid volume within the cell                                                                                |
+-------------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``vt``            | ``IN``  | ``W_P`` | scalar representing the total volume of the polyhedron                                                                                      |
+-------------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``vertp``         | ``IN``  | ``W_P`` | array of dimensions :math:`({nv},3)` storing the :math:`x,y,z`-coordinates of each vertex                                                   |
+-------------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``xnc, ync, znc`` | ``IN``  | ``W_P`` | :math:`x,y,z`-components of the unit-length vector :math:`\boldsymbol{n}` normal to the PLIC interface pointing towards the liquid phase    |
+-------------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``xns, yns, zns`` | ``IN``  | ``W_P`` | arrays of length :math:`\texttt{ns}` storing the :math:`x,y,z`-components of the outward-pointing unit normal vector for each face boundary |
+-------------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** This routine is intended for the original, untruncated cell geometry, with (:math:`\texttt{ntp}=\texttt{ntv}`). The total cell volume must satisfy :math:`\texttt{vt}>0`, and the target liquid volume must satisfy :math:`0\leq \texttt{v}\leq \texttt{vt}`. The argument :math:`\texttt{v}` is a volume, not a volume fraction; for a prescribed liquid volume fraction :math:`\alpha`, use :math:`\texttt{v}=\alpha\,\texttt{vt}`.

If :math:`\texttt{vt}\leq0` or :math:`\texttt{ntp}>\texttt{ntv}`, the routine prints a diagnostic message and returns without assigning a valid value to ``c``.
