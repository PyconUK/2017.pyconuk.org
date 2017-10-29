original_id: 9DE8
title: "Automated data exploration"
subtitle: "Building scalable and efficient analysis pipelines with Dask"
speaker: victor-zabalza
track: pydata
video:
slides: https://www.slideshare.net/VictorZabalza/automated-data-exploration-building-efficient-analysis-pipelines-with-dask-81328214
---
The first step in any data-intensive project is understanding the available data. To this end, data scientists spend a significant part of their time carrying out data quality assessments and data exploration. In spite of this being a crucial step, it usually requires repeating a series of menial tasks before the data scientist gains an understanding ofthe dataset and can progress to the next steps in the project.

In this talk I will detail the inner workings of a Python package that we have built which automates this drudge work, enables efficient data exploration, and kickstarts data science projects. A summary is generated for each dataset, including:

- General information about the dataset, including data quality of each of the columns;
- Distribution of each of the columns through statistics and plots (histogram, CDF, KDE), optionally grouped by other categorical variables;
- 2D distribution between pairs of columns;
- Correlation coefficient matrix for all numerical columns.

Building this tool has provided a unique view into the full Python data stack, from the parallelised analysis of a dataframe within a Dask custom execution graph, to the interactive visualisation with Jupyter widgets and Plotly. During the talk, I will also introduce how Dask works, and demonstrate how to migrate data pipelines to take advantage of its scalable capabilities.
