original_id: 9DEE
title: "I think I wrote a Rapid Web-Application Development tool"
subtitle: "Was it a mistake?"
speaker: emma-delescolle
track:
video: https://www.youtube.com/watch?v=H_EPck2VIM4
slides: http://bit.ly/djember-RAD
---
It all started with someone asking me about configuring a well known python ERP system for managing members of an organisation.
My answer was that configuring a full-blown ERP for this kind of task was most likely too much of a hassle and that Django would probably be better suited for that kind of job.

After that, since Django comes with built-in functionalities used by the core of most ERP systems, I started wondering how Django would fare to manage more complex things than a "simple users list" and started the task building a full enterprise management system for our small company. Of course, this is not what the original Django developers had in mind when they wrote it and therefore it has some limitations for that use-case. Some of those limitations can be addressed with existing plugins, others can't.

For the past couple of years I've been assembling some libraries (both python and javascript) in order to help me build this management system that could "handle anything". After the fact, when I look back at the work that has been done, it looks a lot like a Rapid Web Application Development tool.

At some point in our tech life, we all decide it would be better to write something "from scratch" rather than using existing tools. Usually it helps us learn new concepts and technologies and is always worth it. The end-result though, often means significant effort and the initial goals are not always met.
