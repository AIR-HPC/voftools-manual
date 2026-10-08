3.30 ``polout2d`` – Polygon geometry export in two-column format
================================================================

.. _polout2d:

The ``polout2d`` routine exports the geometric data of a polygon to an external file in a standard two-column ASCII format (e.g., :math:`x,y` coordinates). This lightweight format is compatible with visualization tools such as ``Gnuplot`` [\ :ref:`16 <bib-gnuplot>`\ ]. The file is written to the current working directory. Its name consists of the prefix ``pol``, the identifier ``ifile`` formatted as five digits with leading zeros, and the extension ``.out``. For example, :math:`\texttt{ifile} = 1` produces ``pol00001.out``. Use identifiers in the range :math:`0 \le \texttt{ifile} \le 99999`.

**Fortran:**

.. code:: fortran

   call polout2d(ifile,ipv,ntv,vertp)

**C:**

.. code:: c

   polout2d(&ifile,ipv,&ntv,vertp);

**Python:**

.. code:: python

   voft.polout2d(ifile,ipv,ntv,vertp) 

**Arguments:**

+-----------+--------+---------+--------------------------------------------------------------------------------------------------+
| ``ifile`` | ``IN`` | ``I_P`` | scalar representing the integer identifier used to name the output file (e.g., ``pol00001.out``) |
+-----------+--------+---------+--------------------------------------------------------------------------------------------------+
| ``ipv``   | ``IN`` | ``I_P`` | array of length ``nv`` storing the vertex indices defining the polygon                           |
+-----------+--------+---------+--------------------------------------------------------------------------------------------------+
| ``ntv``   | ``IN`` | ``I_P`` | total number of vertices in the polygon                                                          |
+-----------+--------+---------+--------------------------------------------------------------------------------------------------+
| ``vertp`` | ``IN`` | ``W_P`` | array of dimensions :math:`({nv},2)` storing the :math:`x,y`-coordinates of each vertex          |
+-----------+--------+---------+--------------------------------------------------------------------------------------------------+

**Note:** The file contains three header lines beginning with :math:`\#`, followed by the vertex coordinates in the order specified by the first ``ntv`` entries of ``ipv``. The first vertex is repeated at the end to close the polygon, giving :math:`\texttt{ntv} + 1` coordinate rows. Coordinates are written in two columns with six decimal places.
