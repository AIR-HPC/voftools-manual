3.1 Module integration and usage
================================

``VOFTools`` provides the Fortran modules ``voftools_mod`` and ``uservoftools_mod``. Their corresponding ``.mod`` files are generated during compilation. For C interoperability, the header files ``cvoftools.h`` and ``cuservoftools.h`` provide the declarations needed to call the Fortran routines from C programs.

3.1.1 Usage in Fortran
----------------------

To utilize ``VOFTools`` within a Fortran program, include the appropriate modules as shown in Listing \ :ref:`3.1 <listing:fortran_example>`\ .

.. _listing:fortran_example:

.. code:: fortran

   program fortran_example
     use voftools_mod !- Main VOFTools module
     use uservoftools_mod !- User-defined routines module
     use, intrinsic :: iso_c_binding,only:w_p => c_double,i_p => c_int
     implicit none
     ! Declare variables using the kind aliases defined above
     ! Invoke the routines and functions, e.g.:
       call voftoolslogo
     !... other routine calls
   end program fortran_example

3.1.2 Usage in C
----------------

To utilize ``VOFTools`` within a C program, include the provided headers as shown in Listing \ :ref:`3.2 <listing:c_example>`\ .

.. _listing:c_example:

.. code:: c

   #include <stdio.h>
   #include "cvoftools.h" // Header for core VOFTools routines
   #include "cuservoftools.h" // Header for  user-defined routines
   int main() {
     // Retrieve array dimensions
     int ns,nv;
     voftools_dim3d(&ns,&nv);
     // Declare required variables
     // Invoke the routines and functions, e.g.:
     voftoolslogo();
     //... other routine calls
     return 0;
   }

The header ``cvoftools.h`` declares the core ``VOFTools`` routines. Include the header ``cuservoftools.h`` when using routines from ``uservoftools_mod``. Compilation and linking follow the procedure described in Section \ :ref:`2.2 <sec:cf-installation>`\ .

3.1.3 Usage in Python
---------------------

``VOFTools`` is exposed to Python via the ``voftools`` package, which wraps the underlying Fortran routines using ``f2py``. Users can import the module as shown in Listing \ :ref:`3.3 <listing:python_example>`\ . Use ``NumPy`` arrays with the shapes and data types required by each routine. Multidimensional arrays passed as ``INOUT`` arguments must be writable and Fortran-contiguous so that ``f2py`` can modify them in place. Such arrays can be allocated with ``order='F'``. For input-only arrays, ``f2py`` may create a temporary copy to convert the data type or memory layout required by the Fortran routine. For efficiency, create multidimensional input arrays in Fortran order with the required data type, particularly when they are reused across multiple routine calls. This avoids unnecessary internal copies.

.. _listing:python_example:

.. code:: python

   import numpy as np
   from voftools import voftools_mod as voft
   #. Retrieve array dimensions
   (ns,nv) = voft.voftools_dim3d()
   #. Invoke the routines and functions, e.g.:
   voft.voftoolslogo()
   #... other routine calls

.. _note-1:

Note:
^^^^^

In what follows, it is assumed that the ``voftools_mod`` module has been loaded as indicated in the previous example.
