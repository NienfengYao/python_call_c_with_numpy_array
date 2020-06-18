# python_call_c_with_numpy_array
Calling a C function from python with numpy arrays as arguments

* Build & Run
  * gcc -fPIC -shared -o module.so module.c 
  * python module.py

* Reference:
  * [Calling C Function from Python](https://www.journaldev.com/31907/calling-c-functions-from-python)
  * [Calling a C function from python with numpy arrays as arguments is easy](https://theferrettouch.wordpress.com/2013/05/04/call-a-c-function-from-python-with-numpy-arrays-as-arguments-is-easy/)
  * [C-Types Foreign Function Interface (numpy.ctypeslib)](https://numpy.org/doc/stable/reference/routines.ctypeslib.html)
    * ndpointer: Array-checking restype/argtypes
  * [Numpy: Data types](https://numpy.org/devdocs/user/basics.types.html)
    * np.uintp(Numpy type) = uintptr_t(C type). Integer large enough to hold a pointer.
  * [Numpy: The Array Interface](https://numpy.org/doc/stable/reference/arrays.interface.html)
    * This page describes the numpy-specific API for accessing the contents of a numpy array from other C extensions.
    * __array_interface__
      * data: A 2-tuple whose first argument is an integer that points to the data-area storing the array contents.
      * strides: a C-style contiguous array or a Tuple of strides which provides the number of bytes needed to jump to the next array element in the corresponding dimension.
