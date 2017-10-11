original_id: C275
title: "Implementing Custom Containers"
subtitle: "No, not Docker, Python collections"
speaker: claus
track: 
video:
---
One often encounters the following situation(s):
- I want to read, load or somehow get data,
- I want to write, dump or somehow save data, 
- I want to iterate over data.

Instead of inventing a completely new class that provides the required functionality, it may make sense to mimic or subclass an already existing collection, e.g. a `dict`, add custom dunder (double underscore) methods and quickly end up with a container that not only serves your purpose but is also very natural to use.

The first part of the talk is devoted to a small tour through the collections module and a presentation of the most important dunder methods that define a container’s behaviour.
The second part is driven by an example that shows how a customized, dict-like container, where set and and get operations are actually read and write operations, can be implemented.
Finally, a few further examples how collections-related dunder methods can be (ab)used conclude the talk.