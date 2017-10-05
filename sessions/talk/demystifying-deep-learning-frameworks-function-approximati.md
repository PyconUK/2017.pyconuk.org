title: "Demystifying Deep Learning Frameworks : Function Approximati"
subtitle: "Generic Function Approximation using Tensorflow"
speaker: siddhartha-rai
track: 
video:
---
This talk attempts to demystify some aspects of Deep Learning using Tensorflow, a popular deep learning framework. Under the hood, Tensorflow is essentially a way to approximate functions. We show how Tensorflow can be used as a generic function approximation tool, and some approaches to tune it.

I propose to cover the following topics in the talk - 

1. How to use Tensorflow to model an arbitrary function
2. Some of the model tuning choices
3. The effect of various tuning choices on the quality and convergence of the optimization algorithm.
4. Most importantly, this talk demonstrates that it is possible to use the same neural network to approximate different types of functions - cubic, quassi-periodic, and exponential
.
As practitioners and users of deep learning frameworks, this should give us the confidence and encouragement, that an appropriately defined deep learning network is capable of being a universal function approximator - i.e. even in the absence of any prior information between the relationship between the input and output, a deep learning network is capable of learning the relationship using the given training data.