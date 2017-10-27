original_id: 54CE
title: "Machine Learning as a Service"
subtitle: ""
speaker: anand-chitipothu
track: 
video:
---
One of the common pain points that we have come across in organizations is the last-mile delivery of data science applications. There are two common delivery vehicles of data products – dashboards and APIs.

More often than not, machine learning practitioners find it hard to deploy their work in production and full stack developers find it hard to incorporate machine learning models in their pipeline. To be able to successfully do a data science-driven product/application, it requires one to have a basic understanding of machine learning, server-side programming and front-end application.

In this workshop, one would learn how to build a seamless end-to-end data driven application – Starting from data ingestion, data exploration, creating a simple machine learning model, exposing the output as a RESTful API and deploying the dashboard as a web application – to solve a business problem.

**Outline:**

1: Introduction and Concepts

* Approach for building ML products
* Problem definition and dataset
* Build the ML Model

2: Build an ML Service

* Concept of ML Service
* Deploy the ML Service - localhost API

3: Build a Dashboard

* Create a simple dashboard
* Integrate ML model API with dashboard

4: Deploying to Cloud

* Deploy the ML service as cloud API
* Deploy the dashboard as cloud service

5: Wrap-up

* Best practices and challenges in building ML service
* Where to go from here

**Required Setup**

All the participants are requested the clone the below mentioned github repo of this tutoriail and install all the required software.

1. Clone the github repo of the tutorial
    
    git clone git://github.com/amitkaps/full-stack-data-science

2. Install [Ananconda for Python 3.5 or 3.6](https://www.continuum.io/downloads) for the workshop. 

3. Install the required packages using conda

    conda install numpy pandas matplotlib seaborn scikit-learn pydotplus flask flask-wtf

4. Install couple of more dependencies from pip

    pip install firefly-python rorolite

Please make sure you do all this before the tutorial starts.



