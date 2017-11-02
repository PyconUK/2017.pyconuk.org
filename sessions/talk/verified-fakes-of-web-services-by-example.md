original_id: C28C
title: "Verified fakes of web services by example"
subtitle: ""
speaker: adam-dangoor
track: 
video:
slides: https://www.slideshare.net/AdamDangoor/adam-dangoor-verified-fakes-of-web-services
---
If your code calls a third party service then you may want to test that your code works but you don't want to call the service in your tests.

It may be expensive, slow or impossible to call that service. For example, if you are making a Slack bot, you want to create tests which don't make calls across the network to Slack.

One approach is to create a mock of that service. Our tests can now run quickly, cheaply and reliably. But if we copy the service incorrectly, or if the service changes, our tests will pass while our code does not work.

Verified fakes solve this problem. You can write tests which confirm that your mock is an accurate representation of the service being mocked. Those tests can be a small subset of your test suite and they can be run periodically, to verify the validity of the many tests which use the mock.

This talk will follow the example of VWS-Python, a verified fake for a proprietary web service. It will discuss the practicalities of creating such a fake and it will focus on the trade-offs, tooling, and approaches involved.

By the end of this talk, the audience will understand how to tie together `pytest`, Travis CI, `requests` and `Responses` to create a verified fake.
  
The talk is aimed at people who have an interest in writing correct software. It is assumed that the audience is familiar with basic testing techniques.