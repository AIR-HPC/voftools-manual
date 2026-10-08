3.6 ``enforvppa`` – PPIC interface location for arbitrary polyhedra
===================================================================

The ``enforvppa`` routine addresses the VCE problem in 3D, specifically aiming to locate the PPIC interface within an arbitrary polyhedral cell. The PPIC interface is defined within a local reference system :math:`(\texttt{u},\texttt{v},\texttt{f})` as:

.. _eq:parab:

.. math::

   \texttt{f}=c_1+c_2\texttt{u}+c_3\texttt{v}+c_4\texttt{u}^2+c_5\texttt{u}\texttt{v}+c_6\texttt{v}^2, \tag{3.1}

where the coefficient :math:`c_1=\texttt{c}` is computed by the routine to ensure that the volume of liquid within the polyhedral cell matches the target volume :math:`\texttt{vf}`. This calculation employs an improved version of the paraboloid-polyhedral approximation procedure based on recursive local grid refinement of the polyhedral cell proposed by [\ :ref:`14 <bib-lopez26>`\ ].

**Fortran:**

.. code:: fortran

   call enforvppa(c,cparab,ie,ipv,nc,nipv,ntp,nts,vf,vt,vertp, &
                 xns,yns,zns)  

**C:**

.. code:: c

   enforvppa(&c,cparab,&ie,ipv,&nc,nipv,&ntp,&nts,
             &vf,&vt,vertp,xns,yns,zns);  

**Python:**

.. code:: python

   (c,ie) = voft.enforvppa(cparab,ipv,nc,nipv,ntp,nts,vf,vt,vertp,xns,yns,zns)  

**Arguments:**

+-------------------+---------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``c``             | ``OUT`` | ``W_P`` | scalar corresponding to the coefficient :math:`c_1` in Eq. (\ :ref:`3.1 <eq:parab>`\ ), representing the conservative position of the paraboloid interface along the local :math:`\texttt{f}`-axis                                                              |
+-------------------+---------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``cparab``        | ``IN``  | ``W_P`` | :math:`12`-component array containing: the six paraboloid coefficients defining the surface geometry (see Eq. \ :ref:`3.1 <eq:parab>`\ , indices ``1--6``); the three components of the unit vector along the local ``f``-axis, expressed in global coordinates |
|                   |         |         |                                                                                                                                                                                                                                                                 |
|                   |         |         | (indices ``7--9``); and the three coordinates of the local origin in global coordinates (indices ``10--12``)                                                                                                                                                    |
+-------------------+---------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ie``            | ``OUT`` | ``I_P`` | integer status flag: 0 indicates successful convergence; 1 indicates failure to find a root                                                                                                                                                                     |
+-------------------+---------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ipv``           | ``IN``  | ``I_P`` | array of dimensions ``(ns,nv)`` storing the vertex indices defining each face boundary.                                                                                                                                                                         |
+-------------------+---------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``nc``            | ``IN``  | ``I_P`` | scalar specifying the number of sub-cells along each coordinate axis of the superimposed Cartesian grid used for the refinement process                                                                                                                         |
+-------------------+---------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``nipv``          | ``IN``  | ``I_P`` | array of length :math:`\texttt{ns}` storing the number of vertices per face boundary                                                                                                                                                                            |
+-------------------+---------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ntp``           | ``IN``  | ``I_P`` | maximum vertex index in the connectivity list                                                                                                                                                                                                                   |
+-------------------+---------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``nts``           | ``IN``  | ``I_P`` | total number of face boundaries                                                                                                                                                                                                                                 |
+-------------------+---------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vf``            | ``IN``  | ``W_P`` | scalar representing the target liquid volume within the cell                                                                                                                                                                                                    |
+-------------------+---------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vt``            | ``IN``  | ``W_P`` | scalar representing the total volume of the polyhedron                                                                                                                                                                                                          |
+-------------------+---------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vertp``         | ``IN``  | ``W_P`` | array of dimensions :math:`({nv},3)` storing the :math:`x,y,z`-coordinates of each vertex                                                                                                                                                                       |
+-------------------+---------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``xns, yns, zns`` | ``IN``  | ``W_P`` | arrays of length :math:`\texttt{ns}` storing the :math:`x,y,z`-components of the outward-pointing unit normal vector for each face boundary                                                                                                                     |
+-------------------+---------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** The first component of ``cparab`` provides the initial estimate of :math:`c_1`. The routine returns the computed coefficient in ``c`` without modifying ``cparab``. After checking that :math:`\texttt{ie}=0`, update ``cparab(1)`` in Fortran or ``cparab[0]`` in C and Python before using the reconstructed interface in subsequent calculations. The component indices in the argument description follow Fortran’s one-based indexing.

The routine assumes the original, untruncated cell geometry, with contiguous vertex indices from 1 to ``ntp``. The subdivision parameter ``nc`` must be a positive integer. The total cell volume must satisfy :math:`\texttt{vt}>0`, and the target liquid volume must satisfy :math:`0\leq \texttt{vf}\leq \texttt{vt}`. Here, ``vf`` denotes a volume, not a volume fraction.

Always check ``ie`` before using ``c``. If :math:`\texttt{ie}=1`, the routine has not obtained an acceptable solution, and ``c`` must not be used as a successfully reconstructed interface.
