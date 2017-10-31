original_id: C275
title: "Implementing Custom Containers"
subtitle: "No, not Docker, Python collections"
speaker: claus
track:
video:
slides: https://github.com/caichinger/slides/tree/master/2017-10-26__PyCon_UK
---
One often encounters the following situation(s):
- I want to represent my data,
- I want to read/write, load/dump or somehow get/save data,
- I want to iterate over data.

Instead of inventing a completely new class that provides required functionality, it may make sense to mimic or subclass an already existing collection, e.g. a `dict`, add custom dunder (double underscore) methods and quickly end up with a container that not only serves your purpose but is also very natural to use.

After a short introduction in which we clarify some notions, we focus on two sample use cases:
- How to extend a tuple to represent data?
- How to implement a dict-like container for data handling?

Throughout the talk we will discover some of the most often needed dunder methods that define a container's behaviour.

**[Slides](https://github.com/caichinger/slides/blob/master/2017-10-26__PyCon_UK/CustomCollections.ipynb)**
