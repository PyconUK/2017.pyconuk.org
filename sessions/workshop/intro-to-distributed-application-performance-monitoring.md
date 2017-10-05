title: "Intro to Distributed Application Performance Monitoring"
subtitle: ""
speaker: hauglustaine
track: 
video:
---
Tracing is a specialized form of logging that is designed to work effectively in large, cloud-scale distributed environments. When done right, traces follow the path of a request across process and service boundaries. This provides a big step-up in application observability, and can help inform a developer why certain requests are slow, or give insights on why they might have behaved unexpectedly.

This session will familiarize attendees with the benefits of tracing, and describe a general toolkit for emitting traces in Python. Matt will walk us through a simple example app, which receives an HTTP request, and gradually instrument it to be observable via traces. Then, we will add a second service, and demonstrate distributed tracing, i.e. traces that cross service boundaries.

We will discuss how context managers and decorators can be used to generate traces and give users hints on how they might add tracing to their own applications and libraries.

In the process users will become familiar with the benefits of tracing your application in production, and some of the challenges involved in adhering to this practice in a distributed environment.