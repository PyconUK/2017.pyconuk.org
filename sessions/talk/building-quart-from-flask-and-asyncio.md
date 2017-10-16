original_id: 54C8
title: "Building Quart from Flask and Asyncio"
subtitle: "Lessons learnt reimplementing Flask using asyncio"
speaker: phil-jones
track: 
video:
---
The Python world is moving towards asyncio web (micro) frameworks, with Sanic and Aiohttp leading the way. Sadly the best (IMO) micro framework, Flask, is incompatible with asyncio. The [Quart](https://gitlab.com/pgjones/quart) framework aims to solve this by reimplementing the Flask API using asyncio. 

I intend to talk about the lessons and difficulties encountered with Flask, Asyncio and the combination. Detailing the difficulties calling coroutines from synchronous functions, and the eventual workaround, how the crux of Flask, global thread locals, have equivalents and how they work, finishing with a discussion about how Python monkey patching allows for some of the Flask extensions to work.