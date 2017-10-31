original_id: C280
title: "What I learned building Forth in 64-bit Intel assembly"
subtitle: "an excursion into what happens when one quirky language from the 1970s becomes a strange urge and a silly side-project"
speaker: david-jones
slides: https://github.com/drj11/forth-pyconuk2017
track: 
video:
---
The computer programming language Forth
was invented by Charles H. Moore
in 1970.
Forth is famous for being _stack based_ and using
_reverse polish notation_:
the _operators_ come after their _operands_.
A Forth program to convert
from Fahrenheit to Celsius (C = (F-32) × 5/9) is:

`32 - 5 * 9 /`

On 23rd August 2016 I had an urge
to write a Forth system
in 64-bit Intel Assembly.
This talk is about what happens next.

In it I unpack what it means to implement a language.
I dig a little into a lower-level description
of typical computer hardware,
and a little into 64-bit Intel Assembly.
Compared to Python,
Forth is a low-level language;
compared to Assembly,
Forth is a high-level language.

I'll talk about how we can implement
one language in terms of another,
by building _models_,
and how we can model languages
and model computational processes.

Forth is a tiny, but powerful, language.
Moore's insight was to discover a language that was:
- small;
- sufficient;
- easy to implement;
- extensible.

The result is that Forth implementations are
typically composed of a tiny nucleus (typically in Assembly)
surrounded by a larger amount of "Forth-in-Forth".

Come. Let's implement a language.
