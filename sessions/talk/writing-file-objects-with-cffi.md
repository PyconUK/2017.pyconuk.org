original_id: 3043
title: "Writing file objects with CFFI"
subtitle: ""
speaker: daniel-pope
track: 
video:
---
This session will be an introduction to CFFI, taking the example of writing file-like objects that read and write byte streams.

CFFI is a binding generator for writing C code extensions for Python, which work on a range of Python interpreters including PyPy.

File-like objects are Python's protocol to read and write streaming data, which you'll be familiar with from open() and StringIO, among many others.

We will learn how to use CFFI to wrap a simple C API, and adapt it to a file object API. To do this we will also need to understand how to use bytes, bytearray and memoryview objects to minimise copying.