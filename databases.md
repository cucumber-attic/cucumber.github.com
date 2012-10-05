---
layout: bootstrap
title: Databases
---
## {{page.title}}

Data stored in one scenario shouldn't be available to the next scenario. This just makes your scenarios brittle and impossible to run in isolation.

There are two ways you can achieve this. Either by deleting all data in a [Before Hook](/hooks.html#before) or (if your database supports it) 

### Transactions

If your database supports transactions, you can tell Cucumber to start a transaction in a [Before Hook](/hooks.html#before) and roll it back 
in an [After Hook](/hooks.html#after). This is such a common thing to do that several Cucumber extensions provide ready-to-use
[Tagged Hooks](/hooks.html#tagged-hooks) using a tag named `@txn`. To enable it you have to tag every [Feature](/gherkin.html#feature) or [Scenario](/gherkin.html#scenario) that needs transactions with `@txn`:

{% highlight gherkin %}
@txn
Feature: Let's write a lot of stuff to the DB
  Scenario: I clean up after myself
    Given I write to the DB
  Scenario: And so do I!
    Given I write to the DB
{% endhighlight %}

#### Cucumber-Rails

Use DatabaseCleaner.

#### Spring-Tx (Cucumber-JVM)

The `@txn` hooks aren't on your [Glue Code Path](/api.html#glue-code) by default, so you have to add it yourself. Just add `cucumber.runtime.java.spring.hooks` to your [Configuration Options](/api.html#configuration) and you're all set:

##### Using JUnit

{% highlight java %}
@RunWith(Cucumber.class)
@Cucumber.Options(glue = {"your.own.glue.code", "cucumber.runtime.java.spring.hooks"})
public class RunCukesTest {
}
{% endhighlight %}

##### Using the CLI

{% highlight text %}
--glue cucumber.runtime.java.spring.hooks
{% endhighlight %}


Note that you must have the `cucumber-spring` module on your `CLASSPATH` in order for this to work.

See the [spring-txn](#) example in Cucumber-JVM for a minimal setup.
