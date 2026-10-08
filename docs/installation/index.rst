2 Installation
==============

.. _installation:

To install the ``VOFTools`` library and run the provided test programs in Fortran, C, and Python, follow the steps outlined below.

Note that the core routines utilize pre-allocated arrays for face indices (``ns``) and vertex indices (``nv``), with default limits of 140 and 200, respectively. While these limits are sufficient for many applications, including computational fluid dynamics (CFD), users requiring support for significantly higher-complexity polyhedral cells may need to adjust the default values.

.. toctree::
   :maxdepth: 2

   /installation/python
   /installation/fortran-c
