original_id: 302F
title: "Testing in Scientific / Engineering Applications"
subtitle: "Interactive vs? test driven development"
speaker: claus
track: 
video:
---
## [Workshop GitHub Repo](https://github.com/caichinger/scipy_testing)


## Setup

Please make sure you have the [repo](https://github.com/caichinger/scipy_testing) 
cloned and the environment specified in 
[env.yml](https://github.com/caichinger/scipy_testing/blob/master/env.yml) 
set up prior to the workshop. 

If you use conda, you can do

```
conda env create --file env.yml
(source) activate scipytesting
```


## Abstract

### Goals

Primary Goal:

> How can I integrate testing in my interactive development process?


Non-Goal:

> How can I do this or that kind of test or how does this particular feature of 
*test work?


### Motivation & Content

Software testing is an undisputed corner stone of software development. 
However, as I know from my personal experience, Python users with a 
non-software-engineering or otherwise scientific background are often not so 
familiar with the concept of testing.

Computational problems are regularly approached by means of interactive 
development, which is both fast and fun and one of the reasons why Python is so 
successful in a wide range of scientific/engineering areas. The widespread 
adoption of the [IPython](http://ipython.org/) and 
[Jupyter](http://jupyter.org/) project are living proof of that.

When carrying out computations, “testing” is implicitly carried out by 
“looking at the result” - which, on a small range, works pretty well. Yet, 
this is not what is meant automatic tests.

Writing tests beforehand, as suggested by 
[Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development)
(TDD), is sometimes considered clumsy and an approach that does not align very 
well with the experimental nature of interactive development. Yet, without 
tests one may quickly get lost in the complexity of even rather small problems.

In this workshop I want to share my personal experience with testing in 
scientific/engineering applications and how testing works for me using
tools like [engarde](http://engarde.readthedocs.org/), 
[doctest](https://docs.python.org/3/library/doctest.html), 
[pytest](http://pytest.org/) and 
[hypothesis](http://hypothesis.readthedocs.org/).

The workshop focuses on the question "How can I integrate testing in my 
interactive development process?".

After a general introduction, each of the above libraries will be employed 
to solve some small exercises to prepare the ground for a slightly more complex 
computational problem which is then approached in an interactive- and 
test-writing-manner.


### Target audience

Engineers/Scientists/People doing interactive development that feel they 
should write tests but either do not know how to do so or think tests stand in 
their way of writing awesome code.


### Disclaimer

This talk is not aimed at professional testers nor is it a (in any way) 
comprehensive introduction to testing.
