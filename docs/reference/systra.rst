3.16 ``systra`` – Rigid-body coordinate transformation
======================================================

The ``systra`` routine transforms the global Cartesian coordinates :math:`(\texttt{x},\texttt{y},\texttt{z})` of a point into local coordinates :math:`(\texttt{f},\texttt{u},\texttt{v})`. The transformation is defined by the orthonormal basis matrix ``vn0``, whose rows contain the local ``f``-, ``u``-, and ``v``-axis unit vectors expressed in global coordinates, and by ``vp0``, the local origin expressed in global coordinates. The transformation is given by:

.. math:: \begin{pmatrix} \texttt{f} \\ \texttt{u} \\ \texttt{v} \end{pmatrix} = \begin{pmatrix} \texttt{vn0}(1,1) & \texttt{vn0}(1,2) & \texttt{vn0}(1,3) \\ \texttt{vn0}(2,1) & \texttt{vn0}(2,2) & \texttt{vn0}(2,3) \\ \texttt{vn0}(3,1) & \texttt{vn0}(3,2) & \texttt{vn0}(3,3) \end{pmatrix} \begin{pmatrix} \texttt{x} - \texttt{vp0}(1) \\ \texttt{y} - \texttt{vp0}(2) \\ \texttt{z} - \texttt{vp0}(3) \end{pmatrix}

**Fortran:**

.. code:: fortran

   call systra(f,u,v,vn0,vp0,x,y,z)

**C:**

.. code:: c

   systra(&f,&u,&v,vn0,vp0,&x,&y,&z);

**Python:**

.. code:: python

   (f,u,v) = voft.systra(vn0,vp0,x,y,z)

**Arguments:**

+---------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``f``, ``u``, ``v`` | ``OUT`` | ``W_P`` | scalars representing the coordinates of a point in the local reference system                                                                                    |
+---------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vn0``             | ``IN``  | ``W_P`` | array of dimensions :math:`(3,3)` whose rows contain the unit vectors of the local ``f``-, ``u``-, and ``v``-axes, respectively, expressed in global coordinates |
+---------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vp0``             | ``IN``  | ``W_P`` | array of length :math:`(3)` storing the origin of the local reference system in global coordinates                                                               |
+---------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``x``, ``y``, ``z`` | ``IN``  | ``W_P`` | scalars representing the coordinates of a point in the global reference system                                                                                   |
+---------------------+---------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** The supplied basis vectors must be mutually orthogonal and of unit length. The routine neither normalizes nor orthogonalizes them.
