title: "Recipes for Productionising Data Science APIs"
subtitle: ""
speaker: andrew-crozier
track: pydata
video:
---
You're a data scientist developing fantastic models with the Python data science stack, and you want to release it into the wild. In this talk, I'll go over some practical solutions to deploying models as HTTP APIs on using the Flask web framework.

Python has the unique advantage of not only being the most widely used language for data science, with a rich and mature stack of numerical and machine learning libraries, but also having a rich ecosystem of tooling for implementing web applications. Merging the best of these two worlds allows us to quickly and easily productionise data science models as APIs.

This talk will be a practical guide for any data scientist or prospective data engineer wanting to productionise data science models, covering:

* Flask
* SQLAlchemy (including integration with Flask with Flask-SQLAlchemy)
* Handling slow computations with job queues in python-rq
* Authorization
* Deployment (including gunicorn)

Code samples implementing a simple application will be provided online following the talk. Participants should be able to use this as a starting point for deploying their own data science APIs online.