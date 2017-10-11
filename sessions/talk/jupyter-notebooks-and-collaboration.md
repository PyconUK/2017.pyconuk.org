original_id: E70D
title: "Jupyter notebooks and collaboration"
subtitle: ""
speaker: scott-stevenson
track: 
video:
---
Git has seen widespread adoption to become the de facto standard for sharing and collaborating on code, and the same is true of Jupyter notebooks as the environment for doing data science. However, herein lies a problem: Git was designed to version plain text files containing source code, and not for storing structured data such as the JSON source of Jupyter notebooks and binary data such as embedded images.

Without extra tooling and processes, this makes following best practices - such as making small, self-contained patches on topic branches and submitting them for code review - difficult, and the output messy. In this talk, I'll demonstrate the tools and practices that make working in data science more collaborative, more productive, and more fun.

I'll show you how to use built-in Git features, such as incremental staging of changed files, to avoid introducing noise from changed cell counts, before moving on to show how simple tooling can allow us to automatically clear output cells from notebooks before committing new changes to Git, avoiding adding binary data to our repository.

Finally, I'll introduce the nbdime tools from the Jupyter project: a set of tools for diffing and merging Jupyter notebooks. I'll demonstrate how to install them, and how to integrate them to Git to finally achieve great integration between Jupyter notebooks and version control for collaborative data science.