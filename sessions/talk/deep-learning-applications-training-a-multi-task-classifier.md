title: "Deep learning applications: training a multi-task classifier"
subtitle: ""
speaker: paulo-eduardo-sampaio
---
Convolutional neural networks are great for image classification. So great, that we want to use a lot of them! The problem is that they are computationally expensive and require the use of GPUs. If you use too many, they can really slow down your data pipeline. Our talk describes how to make use of a deep convolutional neural network to perform multiple classification tasks at once. As a result of sharing a single convolutional stage for multiple tasks, it saves a lot of processing time, whilst performing at a similar level of accuracy. We’ll show you an example using Keras, illustrating the impact in processing time and accuracy, and also some interesting results in the quality of the embedding.
