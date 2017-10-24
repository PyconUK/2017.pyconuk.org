original_id: 0B9A
title: "Intermediate TDD workshop: outside-in, mocking & isolation"
subtitle: "purists vs pragmatists, mocks vs end-to-end tests, let's illustrate all the pros + cons with a real example."
speaker: harry-percival
track: 
video:
---
This session is aimed at an "intermediate" testing audience; labels like intermediate are always a bit dangerous, so to be more specific, I mean people who've learned a bit about testing, have tried it out a bit, and are starting to encounter some of the real-world problems of what to mock and what not to mock, and to wonder about best practices.

This workshop is based on a simple, practical example, where we'll go through a "pragmatic", non-mocky approach, and contrast it with a "purist", highly isolated approach, and see how it illustrates the strength and weaknesses of both approaches.  Hopefully we will conclude with a little discussion of how to get the best out of our tests, based on what it is we want from them.

## preparation required!

this is a hands-on workshop, so come with a laptop and prepared to follow along.  if you don't then the workshop will be quite boring!

Here's what you need:

* Firefox
* [Geckodriver](https://github.com/mozilla/geckodriver/releases)
* A checkout of [the example repo](https://github.com/hjwp/book-example/)
* and a virtualenv with Python 3.6, django and selenium in it.

more details:

1. download the example code and create your virtualenv

```
git clone https://github.com/hjwp/book-example/ tdd-workshop
cd tdd-workshop
git checkout intermediate-workshop-start
mkvirtualenv --python=python3 tdd-workshop  # or however you like to create virtualenvs
pip install -r requirements.txt
```

2. download geckodriver from https://github.com/mozilla/geckodriver/releases, unzipping it and check it works:

```
geckodriver --version
geckodriver 0.19.0
...
```

On windows it's usually fine to just have the binary in the same folder as your
python project (eg next to *manage.py*).  On linux + macos, you'll need to put
the geckodriver binary somewhere on your path and make sure it's executable from anywhere.

There are some more tips and hints in the 
[installations chapter of my book](http://www.obeythetestinggoat.com/book/pre-requisite-installations.html).



3. Take a look around the example site  with:

```
mkdir ../database
python manage.py migrate
python manage.py runserver
```

it's a very simple to-do lists site...

4. Run the test suite and check everything works:
```
pip install selenium
python manage.py test
```

You should see it run 60 tests and all but one should pass. The expected error is `Unable to locate element: My lists`

## If anything doesn't look right, you need to fix it before the workshop!

There are some detailed installation instrutions at http://www.obeythetestinggoat.com/book/pre-requisite-installations.html

If firefox+geckodriver really refuses to work, you can try switching from
`webdriver.Firefox()` to `webdriver.Chrome()`.  You will need to download a
thing called "chromedriver" (google it) and have it on the path.

# I look forward to seeing you on Saturday!

Any problems, do ping me on the conference slack, or email me at obeythetestinggoat@gmail.com

