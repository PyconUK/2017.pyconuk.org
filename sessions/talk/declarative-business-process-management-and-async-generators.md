original_id: C290
title: "Declarative Business Process Management and Async Generators"
subtitle: "Introducing WorkScheme: a Python 3.6 and aiohttp implementation of a lightweight BPM engine using a functional DSL."
speaker: james-skillen
track: 
video: https://www.youtube.com/watch?v=FUH7xtPkQtI
---
BPM engines typically execute BPMN diagrams produced by a process engineer using a GUI. WorkScheme instead defines and interprets a functional domain-specific language based on a subset of Scheme. It also provides BPMN output via compilation to graphviz's dot and inclusion within Sphinx documentation of the process.

Defining features of BPM are supported: concurrency of independent tasks (using asyncio); and persistence of state (pickling a stackless interpreter). Business tasks are provided by imported Python modules.

A novel use for async generators is found as elegantly allowing for complex interaction between process and task. An example is two-phase commit for user interaction, improving robustness versus existing solutions.