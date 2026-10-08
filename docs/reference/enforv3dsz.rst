3.5 ``enforv3dsz`` – Efficient PLIC interface location for orthogonal hexahedral cells
======================================================================================

The ``enforv3dsz`` routine addresses the VCE problem within rectangular parallelepipedic cells, such as those defined in the ``voftools_cube`` routine. It employs the more efficient analytical method proposed by [\ :ref:`20 <bib-scardovelli00>`\ ], which is specifically designed for use with this type of cell.

**Fortran:**

.. code:: fortran

   call enforv3dsz(c,dx,dy,dz,v,vertp,xnc,ync,znc)

**C:**

.. code:: c

   enforv3dsz(&c,&dx,&dy,&dz,&v,vertp,&xnc,&ync,&znc);

**Python:**

.. code:: python

   v = np.array(v, dtype=np.float64)
   c = voft.enforv3dsz(dx,dy,dz,v,vertp,xnc,ync,znc)

**Arguments:**

+------------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``c``                  | ``OUT``   | ``W_P`` | scalar representing the signed distance from the PLIC interface to the origin along the normal vector :math:`\boldsymbol{n}`             |
+------------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``dx``, ``dy``, ``dz`` | ``IN``    | ``W_P`` | cell dimensions along the coordinate axes :math:`x,y,z`                                                                                  |
+------------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``v``                  | ``INOUT`` | ``W_P`` | scalar representing the target liquid volume within the cell; modified internally and restored to its original value before return       |
+------------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``vertp``              | ``IN``    | ``W_P`` | array of dimensions :math:`({nv},3)` storing the :math:`x,y,z`-coordinates of each vertex                                                |
+------------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``xnc, ync, znc``      | ``IN``    | ``W_P`` | :math:`x,y,z`-components of the unit-length vector :math:`\boldsymbol{n}` normal to the PLIC interface pointing towards the liquid phase |
+------------------------+-----------+---------+------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** The cell must be a rectangular parallelepiped with edges parallel to the coordinate axes. Its eight vertices must occupy the first eight rows of ``vertp``, and ``dx``, ``dy``, and ``dz`` must be the corresponding positive side lengths. The target liquid volume must satisfy :math:`0\leq \texttt{v}\leq \texttt{dx}\,\texttt{dy}\,\texttt{dz}`.
