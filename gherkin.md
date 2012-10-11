---
layout: bootstrap
title: Gherkin
---
## {{page.title}}

Gherkin is the format for Cucumber Specifications. Technically speaking it is a [small computer language](http://www.martinfowler.com/bliki/BusinessReadableDSL.html) with a well-defined syntax, but
it's so simple that you don't have to know how to program in order to use it. Here is a simple Gherkin document:

{% highlight gherkin %}
Feature: Password management
  Scenario: Forgot password
    Given a user with email "cukes@cukes.info" exists
    When I ask for a password reset
    Then an email with a password reset link should be sent
{% endhighlight %}

The only syntax here is the colored keywords at the beginning of each line. The rest is entirely up to you.

TODO: MORE