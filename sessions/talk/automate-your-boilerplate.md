original_id: 54C0
title: "Automate your Boilerplate"
subtitle: "Hitting the Ground Running with Project Templating in Data Science"
speaker: chris-musselle
track: pydata
video: https://www.youtube.com/watch?v=kicfCZLxhHA
---
Project templating and scaffolding tools like the cookiecutter Python package can be a great help when starting a new project. They provide a way of generating a predefined layout of files and directories, and can also be parameterised to accept arguments as they are generated. e.g. name of the new project.

Creating such a template takes some effort but means quicker startup times on future projects; less boiler plate code to write; more consistent project layouts; and even automation of common setup tasks. However such templates work best for setting up highly repeatable project structures (like when writing plugins or small command line applications). 

Can we make use of these for Data Science projects? I will share my experience of doing so in this talk, along with the benefits and drawbacks I have found in trying to automate away as much of the boilerplate and manual effort when starting a new Data Science project! 

I will then present how I have eased some of the pain points by breaking down a typical project into several templating layers, and then developing a command line tool to help manage and apply these template layers to a project as and when needed. 

As part of the talk I will give an overview of cookiecutter templates, and how they can be built upon to achieve this approach of composable project templating.