original_id: 7953
title: "Single Malt WSGI"
subtitle: "Enhance your WSGI applications with Talisker"
speaker: simon-davy
track: 
video:
---
This talk will introduce the Talisker project, which is an enhanced WSGI
application runner based on standard python tools.

Production WSGI applications require extras beyond just your
application, like powerful logging, metrics, tracing and error
reporting.  Repeatedly integrating these into each new WSGI
app/microservice can be dull, error prone, and inconsistent across
services.

Talisker aims to provide drop-in best practice support out of the box in
all these areas and more. It integrates a set of popular python web
tools into a single WSGI run-time.

 - gunicorn
 - requests
 - sentry

And optionally:

 - django
 - flask
 - celery
 - statsd
 - prometheus_client

It also uses a novel technique to enhance stdlib's default logging to
support structured logging for all loggers.

Talisker pulls all these tools together, and enhances the whole app. For
example, requests and gunicorn get metrics and request id tracing on
HTTP requests. Even your cron jobs can be run via Talisker, providing
them with structured logging, metrics and error reporting.

Designed to be simple to use, you can use it as a drop in replacement
for gunicorn to run your apps gunicorn to get the benefit, and opt-in to
other features as needed.

The talk will introduce the motivations behind the project, the
decisions we've made, and our experience running a fleet of
microservices with Talisker at Canonical.

More information can be found at https://talisker.readthedocs.io