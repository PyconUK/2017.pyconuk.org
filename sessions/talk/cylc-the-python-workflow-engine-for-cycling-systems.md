original_id: 3046
title: "Cylc: the Python workflow engine for cycling systems"
subtitle: ""
speaker: declan-valters
track: 
video:
---
Cylc ("silk") is a general-purpose Python workflow engine or 'metascheduler'; a system that can automatically execute tasks according to complex schedules and dependencies, and deal with task failures if they occur. We will showcase the applications of Cylc in weather and climate services, and reflect on how its implementation in Python has aided the development of the Cylc software package.

Complex workflows are increasingly at the heart of scientific research and business logic. This is true across a range of industries and scientific disciplines where we find workflows consisting of thousands of tasks which require running to a non-trivial schedule. At the Met Office, for example, we use Cylc to manage weather forecasting and climate research activities, where it has been used to drive operational systems since 2013. Cylc can manage workflows on a variety of computing platforms, from desktop PCs to high-performance computing services, and is currently used to efficiently utilise resources on some of the largest supercomputers in the world. Cylc is an open-source project led by a small team of core developers at the Met Office (UK) and the National Institute of Water and Atmospheric Research (New Zealand). The cylc website can be found at cylc.github.io/cylc/.