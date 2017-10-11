original_id: 54C4
title: "Frictionless Data, Frictionless Development"
subtitle: "Building a scalable data converter, processor and warehouse with tabulator, tableschema-py, kubernetes and flask"
speaker: andrew-stretton
track: pydata
video:
---
A common problem in Data Engineering is how to create a platform capable both of importing and exporting tabular data in numerous formats and of maintaining a change history of the data while users update and query it.

Tools like Trifacta (Google Cloud Dataprep [1]) provide a turnkey solution to part of the pipeline but the open source Frictionless Data [2] tools from OKFN can provide a simpler subset of these features tailored to your requirements.

Just as Pandas [3] is built around the Dataframe, the Frictionless Data approach uses data packages [4] consisting of a JSON table schema and a data URI. These schemata can be easily generated for any dataset and work well for a number of applications such as:

* Validating new data with tools like Goodtables [5] or tableschema-py

* Building a data update interface with tools such as Handontable JS [6]

* Creating declarative data processing pipelines that a front end can
easily interact with via datapackages pipelines [7] and kubernetes [8]

* Pushing data into various databases and repository tools such
as CKAN datastore [9]

* Extending the schema to allow export to linked data formats such as
IIIF

The talk will cover these use cases and compare with the approaches taken by other open-source data science / BI tools such as Datashape [10] with ODO [11] from Continuum and Superset [12] from AirBnB. I will aim to demonstrate that that lightweight web standards like datapackages speed up the development process.

References

   1. https://cloud.google.com/dataprep/
   2. http://frictionlessdata.io/tools/
   3. http://pandas.pydata.org/
   4. http://frictionlessdata.io/data-packages/
   5. http://goodtables.okfnlabs.org/
   6. https://github.com/handsontable/handsontable
   7. https://github.com/frictionlessdata/datapackage-pipelines
   8. https://kubernetes.io/
   9. https://github.com/ckan/ckan/tree/master/ckanext/datastore 
  10. https://github.com/blaze/datashape
  11. https://github.com/blaze/odo
  12. https://github.com/apache/incubator-superset