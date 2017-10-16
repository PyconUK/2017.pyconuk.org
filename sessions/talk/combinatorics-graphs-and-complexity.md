original_id: C27E
title: "Combinatorics, graphs, and complexity"
subtitle: "How to measure complexity, with thanks to Bletchley codebreaker Bill Tutte (1917-2002)"
speaker: jonathan-fine
track: pydata
video:
---
Bill Tutte broke the Lorenz cipher and, after the war, pioneered graph theory and their associated matroids. Each graph G determines a matroid convex polytope G.

For simple convex polytopes, homology provides non-negative integers g[0], g[1], g[2], etc. Each g[i] gives a bound for g[i+1], and if g[i] is zero then so is g[i+1]. These g[i] nicely measure complexity.

Usually, P(G) is not simple. Defining the homology of general convex polytopes is the speaker's main research problem. It's hard.

But all is not lost. Every convex polytope X has a flag vector f(X), as we expect the complexity of a graph to be a linear function of f(P(G)). And we already have part of the g[i].

The speaker hopes this talk contributes to the dialogue between data science and pure mathematics, to the benefit of both sides.