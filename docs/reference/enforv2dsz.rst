3.24 ``enforv2dsz`` – Efficient PLIC interface location for rectangular cells
=============================================================================

The ``enforv2dsz`` routine solves the VCE problem specifically for axis-aligned rectangular cells, such as that defined in the ``voftools_square`` routine. It employs an efficient analytical solution proposed by [\ :ref:`20 <bib-scardovelli00>`\ ], which provides a closed-form expression for the interface position :math:`c` given the normal vector :math:`\boldsymbol{n}=(\texttt{xnc}, \texttt{ync})` and target liquid area :math:`\texttt{v}`.

:math:`\,`

:math:`\,`

**Fortran:**

.. code:: fortran

   call enforv2dsz(c,dx,dy,v,vertp,xnc,ync)

**C:**

.. code:: c

   enforv2dsz(&c,&dx,&dy,&v,vertp,&xnc,&ync);

**Python:**

.. code:: python

   v = np.array(v, dtype=np.float64)
   c = voft.enforv2dsz(dx,dy,v,vertp,xnc,ync)

**Arguments:**

+----------------+-----------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``c``          | ``OUT``   | ``W_P`` | scalar representing the signed distance from the PLIC interface to the origin along the unit normal vector :math:`\boldsymbol{n}`                        |
+----------------+-----------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``dx``, ``dy`` | ``IN``    | ``W_P`` | scalars representing the cell dimensions along the :math:`x` and :math:`y` directions, respectively                                                      |
+----------------+-----------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``v``          | ``INOUT`` | ``W_P`` | scalar representing the target liquid area within the cell; temporarily modified during the calculation and restored to its input value before returning |
+----------------+-----------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vertp``      | ``IN``    | ``W_P`` | array of dimensions :math:`({nv},2)` storing the :math:`x,y`-coordinates of each vertex                                                                  |
+----------------+-----------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``xnc, ync``   | ``IN``    | ``W_P`` | :math:`x,y`-components of the unit-length vector :math:`\boldsymbol{n}` normal to the PLIC interface pointing towards the liquid phase                   |
+----------------+-----------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** The cell must be an axis-aligned rectangle whose four corner coordinates occupy the first four rows of ``vertp``. The positive dimensions ``dx`` and ``dy`` must match its side lengths along the coordinate axes. The prescribed liquid area must satisfy :math:`0 \le \texttt{v} \le \texttt{dx} \texttt{dy}` ; for an area fraction :math:`\alpha`, use :math:`\texttt{v} = \alpha \texttt{dx} \texttt{dy}`.
