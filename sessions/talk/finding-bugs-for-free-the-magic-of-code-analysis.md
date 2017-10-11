original_id: 302E
title: "Finding bugs for free: The magic of code analysis."
subtitle: ""
speaker: mark-shannon
track: 
video:
---
Code analysis is a powerful technique for improving the quality of software. It allows you to find bugs in your Python code that would be very hard to find with testing, and without  the need for any annotations.

In this talk I show examples of "interesting" bugs that we at lgtm.com have found in real code. For each example, I will describe how we can find that type of error.

In order to avoid unnecessary embarrassment, all examples will be anonymised.

Intended Audience
------------------------

Most Python developers.
I will assume that the audience knows Python reasonably well, but knows little or nothing about code analysis.

-------------------

At lgtm.com we provide state-of-the-art analysis for a number of languages including Python. We have found bugs in the standard library, requests, numpy and many others.