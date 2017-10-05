title: "On Big Computation and Python"
subtitle: ""
speaker: russel-winder
track: 
video:
---
Python is a programming language slow of execution but fast of program development – except for some sorts of bug that a statically compiled language catch easily. Lots of science folk are using Python because of ease of development and the great libraries, not to mention the great communities. Big Data has, it seems become a thing, though most scientists still use what are really very small data sets. What about Big Computation, lots of CPU (and GPGPU) cycles, not really a lot of TB of data?

To speed up Python code execution we have Cython (not exactly Python, but…), NumPy (a whole new subsystem, but everyone like Matplotlib), and Numba. But are these really good for Big Computation. Should we be looking as polyglot systems? C is a non-starter. Is C++ good enough? Can Go or Rust help? Is D a player? Have you ever tried Chapel?

In this session we'll try some stuff out, then you can make up your own mind.