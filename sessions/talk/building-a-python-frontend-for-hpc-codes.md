original_id: C286
title: "Building a python frontend for HPC codes"
subtitle: ""
speaker: alice-harpole
track: 
video: https://www.youtube.com/watch?v=tQuiOyTWfkk
---
HPC (high performance computing) codes are widely used in computational science, however they are often difficult to manage, with complex build processes, reliance on multiple input and parameter files and intricate data processing routines to visualise the results. Typical approaches to automating this often involve shell scripts to try and link these different stages together, however these can also end up being quite complex and unreadable, particularly for less experienced users. 

I shall present my experience building a python interface for the AMReX Astro codes, a family of codes for AMR (adaptive mesh refinement) modelling of astrophysical systems. I shall look at how I used python to manage the compilation process, create input data, submit supercomputer jobs and visualise the output.