---
layout: bootstrap
title: Gherkin
---
# {{page.title}}

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
Gherkin documents are stored in regular text files with a `.feature` file extension. The file above could
be stored in a `password_management.feature` file.

When you [run Cucumber](/running.html), it will generate a report that verifies whether or not the software
behaves the way the Gherkin document says.

How is that possible? You (or someone else on your team) can then write [some code](/step-definitions.html)
that translates the text in the Gherkin document into interactions with the software.

TODO: MORE
