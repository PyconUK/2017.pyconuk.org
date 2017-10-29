original_id: 9DE3
title: "Introduction to Survival Analysis with scikit-survival"
subtitle: ""
speaker: sebastian-polsterl
slides: https://k-d-w.org/pyconuk-2017/
track: pydata
video:
---
The aim of survival analysis – also referred to as reliability analysis in engineering – is to analyse the time until one or more events happen. Examples from the medical domain are the time until death, until onset of a disease, or until pregnancy. In engineering, the time until the failure of a mechanical system is a common application. In a typical clinical study, the exact time of an event will remain unknown for a subset of individuals, simply because some remained event-free before the study ended or decided to withdraw from the study. For these patients, it is unknown whether they did or did not experience an event after termination of the study. The only valid information is that any (unobserved) event must have occurred after the study ended. This property needs to be considered when applying machine learning to these type of data.

In this talk, I will give an introduction to survival analysis and demonstrate how to analyse survival data using scikit-survival (https://github.com/sebp/scikit-survival): a Python module for survival analysis built on top of scikit-learn. I will introduce survival data from various domains and explain why traditional regression and classification methods are unsuitable. Using practical examples, I will demonstrate how scikit-survival can be used to estimate the time until an event and how additional variables can be used to improve prediction. Finally, I will give an outlook on more advanced methods, which are suitable to analyse high-dimensional clinical data.
