original_id: 302F
title: "Testing in Scientific / Engineering Applications"
subtitle: "Interactive vs? test driven development"
speaker: claus
track: 
video:
---
Software testing is an undisputed corner stone of software development. However, as I know from my personal experience, Python users with a non-software-engineering or otherwise scientific background are often not so familiar with the concept of testing.

Computational problems are regularly approached by means of interactive development, which is both fast and fun and one of the reasons why Python is so successful in a wide range of scientific/engineering areas. While implementing, “testing” is implicitly carried out by “looking at the result” - which, on a small range, works pretty well. Yet, this is not what is meant by writing tests.

Writing tests beforehand, as suggested by test driven development, is sometimes considered clumsy and an approach that does not align very well with the experimental nature of interactive development. 

In this talk I want to share my personal experience with testing in scientific/engineering applications and how testing works for me (interactive development, TDD/Unit Testing), using pytest (and doctest).

More precisely, the following topics are covered:
- Why testing? How testing aids software development.
- What is testing? The purpose of different kind of tests is outlined and compared.
- How to test? The mechanics of writing and executing a test.
- How to integrate testing in the workflow? Easing the pain and actually profiting from writing tests.
- Selected pytest features I like most.
- Notes on testing numpy.nbarray, pandas.DataFrame objects, coverage and hypothesis.

Target audience:
Engineers/Scientists/People doing interactive development that feel they should write tests but either do not know how to do so or think tests stand in their way of writing awesome code.

Disclaimer:
This talk is not aimed at professional testers nor is it a (in any way) comprehensive introduction to testing.
