# SequenceFormConverterBitcamp2022

## Overview
Input the coefficients and starting values of a recursive formula where each term is a linear combination of any number
of previous terms, and we'll calculate a closed form that approximates it to an estimated +-(10^-8)% error.

## Inspiration
In my 250 class with Gasarch, I was given an assignment to write a program that would find the roots of a recursive formula where each term is a linear combination of the previous two terms. I went a little overboard and submitted a program that would find the whole closed form. In doing so, I generalized my code to work with any coefficients and any starting values. But that got me thinking, could I also generalize it to work with any number of terms? Turns out the answer is yes, and it worked even better than I expected.
## What it does
For a recursive formula where each term is a linear combination of the previous t terms, the pattern described by the formula's coefficients is also exhibited by r^n  for each of t roots r. My program finds these roots by repetitively using the Newton-Raphson method for complex numbers. It then uses linear algebra to find which linear combination of the geometric sequences defined by those roots fulfills the initial values of the recursive formula.
## How I built it
I decided to build my program entirely from scratch using python's builtins. The only tools that I imported were functools.wraps() (to preserve meta-info when using the cache decorator I created), time.sleep() (to make my UI more readable), And the "typing" library to annotate my code. I also used operator overrides in all of my objects to make my code as readable as possible.
## Challenges I ran into
One problem that I ran into was the fact that the Newton-Raphson method only approximates roots to a specified precision, and will usually not get the exact root, which introduces error into the system. Because of the limits of float size in python, the precision can only be so high, giving the closed form calculation an estimated +-(10^-8)% error, which though small, still makes the closed form only an approximation and not an exact representation. On lower terms, this error is hidden because the output is truncated to 5 decimal places.
## Accomplishments that I'm proud of
When I first thought of this project, it was mainly as a joke. But I talked about it with some friends and we started to get all hyped up about whether or not it was possible. I wasn't sure it could be done, but once I had a plan in my mind I had to execute it. That first moment when my solution came together and spit out the Fibonacci Sequence was so cathartic, and my excitement only grew as I threw in more and more initial conditions and watched it accurately approximate all of them.
## What I learned
I learned a lot about operator overriding and building interconnected classes.
## What's next for Sequence Form Converter
This was really just a fun experiment in my capabilities both as a programmer and a mathematician. Though the idea of converting recursive sequences into closed forms is useful generally because it reduces algorithmic complexity when finding terms, simple sequences like the ones I evaluated with this program can be run relatively quickly in their recursive forms. This program can be useful though for teaching about the differences between recursive and closed forms, as well as how to discover the closed form through constructive induction, since that is the method it employs.
