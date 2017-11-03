original_id: 3041
title: "Creating a Python Web-App for Destiny the Game"
subtitle: "Using Python and the Flask Microframework to create a web app for Destiny the Game."
speaker: allyn-hunt
track: 
video: https://www.youtube.com/watch?v=aTV574nBZ4A
---
For the last year and a half I have been working on creating a Python based application for Destiny the game (Play Station, Xbox and soon to be released on PC). I started this project as a practical exercise to increase my knowledge in Python, I have progressed from developing several small scripts, which interface with the game environment, to deploying and managing a Flask based web application.
I have been blogging about my progress with the application since August 2016, creating several how-to guides, a custom OAuth 2.0 flow that is currently being used by several other Destiny applications, and a full web application. My blog has to date received ~45,000 views.
The Destiny developers, Bungie (Destiny, Halo), have released an incredibly powerful API which allows you to interact with your in-game character, collect a huge amount of stats and track all of your activities. I have used the Python Requests library to interface with the game environment via the Destiny API, I use SQLAlchemy to store user account information, and the Jinja2 web templating language for Python, as a web front end.

Application Features:
Login via custom OAuth 2.0 flow (Bungie.net OAuth flow was not compatible with current OAuth libraries).
Store user account details in an SQL database.
View full in-game account details.
View your in-game characters inventory. 
Send a POST request to select another character (each game account can have up-to 3 characters).
View items stored in shared Vault (in game item storage that is available to all of your characters).
Transfer items, change weapons and armour live in game.
View a list of (Play Station or Xbox) friends in your in-game clan. Also view basic account and character details.
View a list of items being sold in-game, receive a HTML formatted email of these items.