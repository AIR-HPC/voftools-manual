3.20 ``polout3d`` – VTK export for polyhedra
============================================

.. _polout3d:

The ``polout3d`` routine exports the geometry and topological data of a polyhedron to an external file in ``VTK`` (visualization toolkit) format [\ :ref:`5 <bib-vtk>`\ ].

The generated files can be visualized using post-processing software such as ``ParaView`` [\ :ref:`3 <bib-paraview>`\ ] [1]_. The filename is automatically generated as ``pol$``\ ``ifile``\ ``.vtk``, where ``$``\ ``ifile``\ ``$`` is the integer identifier provided by the user.

**Fortran:**

.. code:: fortran

   call polout3d(ifile,ipv,nipv,ntp,nts,vertp)

:math:`\,`

**C:**

.. code:: c

   polout3d(&ifile,ipv,nipv,&ntp,&nts,vertp);

**Python:**

.. code:: python

   voft.polout3d(ifile,ipv,nipv,ntp,nts,vertp)

**Arguments:**

+-----------+--------+---------+----------------------------------------------------------------------------------------------------------+
| ``ifile`` | ``IN`` | ``I_P`` | scalar representing the integer identifier used to name the output file                                  |
+-----------+--------+---------+----------------------------------------------------------------------------------------------------------+
| ``ipv``   | ``IN`` | ``I_P`` | array of dimensions ``(ns,nv)`` storing the vertex indices defining each face boundary of the polyhedron |
+-----------+--------+---------+----------------------------------------------------------------------------------------------------------+
| ``nipv``  | ``IN`` | ``I_P`` | array of length :math:`\texttt{ns}` storing the number of vertices per face boundary                     |
+-----------+--------+---------+----------------------------------------------------------------------------------------------------------+
| ``ntp``   | ``IN`` | ``I_P`` | maximum vertex index in the connectivity list                                                            |
+-----------+--------+---------+----------------------------------------------------------------------------------------------------------+
| ``nts``   | ``IN`` | ``I_P`` | total number of face boundaries of the polyhedron                                                        |
+-----------+--------+---------+----------------------------------------------------------------------------------------------------------+
| ``vertp`` | ``IN`` | ``W_P`` | array of dimensions :math:`({nv},3)` storing the :math:`x,y,z`-coordinates of each vertex                |
+-----------+--------+---------+----------------------------------------------------------------------------------------------------------+

**Note:** The file is written to the current working directory. Its name consists of the prefix ``pol``, the identifier ``ifile`` formatted as five digits with leading zeros, and the extension ``.vtk``. For example, :math:`\texttt{ifile} = 1` produces ``pol00001.vtk``. Use identifiers in the range :math:`0 \le \texttt{ifile} \le 99999`.

.. [1]
   The routine generates a legacy ``VTK`` file in ASCII format with dataset type ``POLYDATA``, representing the polyhedron’s polygonal surface.

   For polyhedra with non-convex polygonal faces, viewers like ``ParaView`` may require triangulation for correct rendering. Users are advised to apply a triangulation filter if visual artifacts occur.
