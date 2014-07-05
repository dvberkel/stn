Square Triangle Numbers
=======================

A program to print out square triangular numbers.

Running
-------

You can run the program with the following command

```sh
./stn.py [20]
```

the argument passed is the number of pairs that you want to output.

Background
----------

### Definition

We call *S(m)* the mth triangular number, i.e.

> S(m) = 1 + 2 + 3 + ... + m

By a [famous trick][trick] of [Gauss][], one has

> S(m) = m(m + 1) / 2

### Problem Statement

The problem asks for *m* and *n* such that

> S(m-1) = S(n) - S(m)

A little algebra reveals that this is equivalent to

> S(n) = S(m-1) + S(m) = m^2

The last identity becomes clear from a [proof without words][pww].

In other words, we are looking for a triangular number that is also a
square.

### Pell's Equation

From the formula for the nth triangular number

> S(n) = n(n + 1) / 2

We get, by using the identity *(a - b) (a + b) = a^2 - b^2*

> n (n + 1) / 2 = (n + 1/2 - 1/2)  (n + 1/2 + 1/2) / 2 = [(2n + 1)^2 - 1] / 8

Equating this to the square *m^2*

> (2n + 1)^2 = 8m^2 - 1

Substituting *x = 2n + 1* and *y = 2m* this reduces to

> x^2 - 2y^2 = 1

which is an instance of [Pell's equation][pell]

### Solution

Pell's equation can be solved by means of finding convergents of
the [continued fraction][] expansion of the square root of two.

Using this method and substituting the solutions back into its
original form one gets the recurrence relations as stated below

> s(n) = 6s(n-1) - s(n-2)
> t(n) = 6t(n-1) - t(n-2) + 2

[trick]: http://mathcentral.uregina.ca/QQ/database/QQ.02.06/jo1.html
[Gauss]: http://en.wikipedia.org/wiki/Carl_Friedrich_Gauss
[pww]: http://www.cut-the-knot.org/ctk/pww.shtml
[pell]: http://en.wikipedia.org/wiki/Pell%27s_equation
[continued fraction]: http://en.wikipedia.org/wiki/Pell%27s_equation
