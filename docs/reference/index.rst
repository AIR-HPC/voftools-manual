3 Routines description and usage
================================

``VOFTools`` utilizes the ``ISO_C_BINDING`` standard to ensure compatibility across Fortran, C, and Python interfaces.

.. _tab:typealiases:

**Table 3.1.** Data type aliases.

======== ==================== ====== =======
Alias    Fortran              C      Python
======== ==================== ====== =======
``W_P``  ``REAL(C_DOUBLE)``   double float64
``I_P``  ``INTEGER(C_INT)``   int    int32
``I_P2`` ``INTEGER(C_SHORT)`` short  int16
======== ==================== ====== =======

Table \ :ref:`3.1 <tab:typealiases>`\  defines the aliases for data types used throughout this manual.

To clarify data handling during subroutine calls, the argument intent labels in Table \ :ref:`3.2 <tab:inout>`\  are employed [1]_.

.. _tab:inout:

**Table 3.2.** Argument intent definitions.

+-----------+--------------+-----------------------------------------------------------------+
| Label     | Definition   | Behavior                                                        |
+===========+==============+=================================================================+
| ``IN``    | Input        | Read-only upon entry; remains unchanged by the routine          |
+-----------+--------------+-----------------------------------------------------------------+
| ``OUT``   | Output       | Set by the routine upon return; entry values are ignored        |
+-----------+--------------+-----------------------------------------------------------------+
| ``INOUT`` | Input/Output | Modified in-place; read by the routine and subsequently updated |
+-----------+--------------+-----------------------------------------------------------------+

.. _geometries-description:

**Table 3.3.** Cell geometries considered in the test programs of Section \ :ref:`4 <sec:test-program>`\ .

+-------------------------+----------------------------------------------------------------------+
| **Routine name**        | **Cell geometry**                                                    |
+=========================+======================================================================+
|                         | 3D                                                                   |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_cube``       | Cube                                                                 |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_ihexa``      | Irregular hexahedron                                                 |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_tetra``      | Tetrahedron                                                          |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_dodeca``     | Dodecahedron                                                         |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_icosa``      | Icosahedron                                                          |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_ipol3d``     | Complex polyhedron with 32 vertices and 18 faces                     |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_ncpentapy``  | Non-convex pentagonal pyramid                                        |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_nccubepy``   | Non-convex cell obtained by substracting a pyramid to the cubic cell |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_scube``      | Stellated cube                                                       |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_nchexa``     | Non-convex hexahedron                                                |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_sdodeca``    | Stellated dodecahedron                                               |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_sicosa``     | Stellated icosahedron                                                |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_hcube``      | Hollowed cube                                                        |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_drcube``     | Drilled cube                                                         |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_zigzag``     | Zig zag prism                                                        |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_logo``       | VOFTools logo                                                        |
+-------------------------+----------------------------------------------------------------------+
|                         | 2D                                                                   |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_square``     | Square                                                               |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_hexagon``    | Regular hexagon                                                      |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_tri``        | Irregular triangle                                                   |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_quad``       | Irregular quadrangle                                                 |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_pentagon``   | Irregular pentagon                                                   |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_ihexagon``   | Irregular hexagon                                                    |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_ncquad``     | Non-convex quadrangle                                                |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_ncpentagon`` | Non-convex pentagon                                                  |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_nchexagon``  | Non-convex hexagon                                                   |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_shexagon``   | Stellated hexagon                                                    |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_hsquare``    | Hollowed square                                                      |
+-------------------------+----------------------------------------------------------------------+
| ``voftools_msquare``    | Non-convex multi-square cell                                         |
+-------------------------+----------------------------------------------------------------------+

Once the installation is complete, the ``VOFTools`` routines and functions can subsequently be used in Fortran, C, and Python programs as described below (see the test programs provided in the supplied software).

.. [1]
   Python users must pass the ``INOUT`` parameters as NumPy arrays to be modified in-place.

.. toctree::
   :maxdepth: 2

   /reference/interfaces
   /reference/geometry
   defpol3d </reference/defpol3d>
   enforv3d </reference/enforv3d>
   enforv3dsz </reference/enforv3dsz>
   enforvppa </reference/enforvppa>
   inte3d </reference/inte3d>
   toolv3d </reference/toolv3d>
   intv3d </reference/intv3d>
   intc3d </reference/intc3d>
   inte3dface </reference/inte3dface>
   areaface </reference/areaface>
   intpv3dpa </reference/intpv3dpa>
   box3d </reference/box3d>
   pvfit </reference/pvfit>
   systra </reference/systra>
   cppol3d </reference/cppol3d>
   dist3d </reference/dist3d>
   initf3d </reference/initf3d>
   polout3d </reference/polout3d>
   voftools_dim3d </reference/voftools_dim3d>
   defpol2d </reference/defpol2d>
   enforv2d </reference/enforv2d>
   enforv2dsz </reference/enforv2dsz>
   inte2d </reference/inte2d>
   toolv2d </reference/toolv2d>
   cppol2d </reference/cppol2d>
   dist2d </reference/dist2d>
   initf2d </reference/initf2d>
   polout2d </reference/polout2d>
   voftools_dim2d </reference/voftools_dim2d>
   voftoolslogo </reference/voftoolslogo>
