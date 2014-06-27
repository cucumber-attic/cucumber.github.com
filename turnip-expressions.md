---
layout: bootstrap
title: Turnip Expressions
---

# {{page.title}}

Turnip Expressions is a more human-friendly alternative to [Regular Expressions](http://en.wikipedia.org/wiki/Regular_expression).
They were first introduced by Jonas Nicklas in the [turnip](https://github.com/jnicklas/turnip) tool.

Cucumber (soon) supports Turnip Expressions in [Step Definitions](/step-definitions.html). This document is both an introduction
to Turnip Expressions and a specification to be used by implementors of Turnip Expressions in various programming languages.

TODO: Add examples from the turnip/behat docs and tests.

## Automatic type conversion

It's common in Cucumber to capture strings and numbers. In dynamic languages like Ruby, the value of a capture group `(\d+)` will always be a string, and the user has to call `to_i` to convert it to an int. Turnip Expressions could be smarter about this if we used a different token to denote type:

```
Given 'I have $n cukes in my :thing' do |n, thing|
  # n is a Fixnum
  # thing is a String
end
```
