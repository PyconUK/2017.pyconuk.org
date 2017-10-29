original_id: E721
title: "First Steps in Using Python with Big Data for Teachers"
subtitle: "Introducing Teachers to the Pandas Library"
speaker: david-ames
track: 
video:
---
A two hour(ish)+, hands on session introducing teachers to the ideas behind processing and accessing Big Data through
Python, specifically using Jupyter Notebooks and the Pandas Library.


The concepts underlying Data Science are starting to make their way into both the GCSE and A Level exam
specifications. This session aims to demystify how teachers can begin to bring practical sessions into their lessons
around these ideas. Some prior knowledge of Python would be beneficial. You will need a device capable of running
Jupyter notebooks and pandas (as a minimum)

Even if you're not a teacher, but would like to know more about using the Pandas library and Jupyter Notebooks this
hands on session might be for you.

Before the session you will need to install Jupyter Notebooks on your laptop - details
[here](https://jupyter.readthedocs.io/en/latest/install.html).

You will also need to install pandas, its' supporting libraries and matplotlib as a minimum.

Install details for Pandas [here](https://pandas.pydata.org/pandas-docs/stable/install.html) and matplotlib
[here](https://matplotlib.org/users/installing.html).

You will also need to install HoloViews, details [here](http://holoviews.org/user_guide/Installing_and_Configuring.html).

There are some issues with the version of HoloViews and the version of Bokeh that gets installed by default, the
workaround is downgrade the Bokeh library from version 0.12.10 to version 0.12.9, which should fix the issue (the last
two lines below show one way of doing this).

## TL;DR
Do the following using the pip associated with Python 3 on your machine.

On Linux this was: 

```bash
$ sudo pip3 install jupyter
$ sudo pip3 install pandas
$ sudo pip3 install matplotlib
$ sudo pip3 install 'holoviews[all]'
$ sudo pip3 uninstall bokeh
$ sudo pip3 install bokeh==0.12.9
```
The `$` is there to indicate the command line prompt, don't type it!

**Please check back closer to the date to check if any other packages need installing too.**


