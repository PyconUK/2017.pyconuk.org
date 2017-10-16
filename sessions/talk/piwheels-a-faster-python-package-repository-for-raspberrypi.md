original_id: 9DF5
title: "piwheels: a faster Python package repository for RaspberryPi"
subtitle: "Building a faster Python package repository for Raspberry Pi users by creating ARM platform wheels of everything on PyPI"
speaker: ben-nuttall
track: 
video:
---
piwheels is a Python package repository providing Python wheels natively compiled for the Raspberry Pi's ARM architecture. It solves the problem that "pip install" can take a long time to build packages implemented in C. Wheels are a general solution to this problem, but PyPI does not currently allow maintainers to upload ARM platform wheels.

I wrote some tooling for automating the building of all 115,000+ packages on PyPI, including all version releases, which totals up to over 750,000 package builds, monitoring the build status and logging the output.in a database, and providing the wheels in a pip-compatible web server. Raspberry Pi users can now "pip install" from this server (a Raspberry Pi) and get pre-built Python wheels, which take just seconds to install.

The first build run I completed was on a Raspberry Pi in my living room: I built the latest version of every package (110k). Then, in order to build all versions of all packages (750k), I moved the project to a cluster of 20 Raspberry Pis in a data centre.