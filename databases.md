---
layout: bootstrap
title: Databases
---
# {{page.title}}

Data stored in one scenario shouldn't be available to the next scenario. This just makes your scenarios brittle and impossible to run in isolation.

This can be done either by deleting all data in a [Before Hook](/hooks.html#before) (running _before_ each Scenario) or to wrap a transaction (if your database supports it) _around_ each Scenario.

## Transactions

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

<ul class="nav nav-tabs">
  <li><a href="#txn-rails" data-toggle="tab" class="rails"><div>&nbsp;</div></a></li>
  <li><a href="#txn-spring" data-toggle="tab" class="spring"><div>&nbsp;</div></a></li>
</ul>

<div class="tab-content">
  <div class="tab-pane" id="txn-rails">
Use DatabaseCleaner.
  </div>
  <div class="tab-pane" id="txn-spring">
The <code>cucumber-spring</code> module contains <code>@txn</code> hooks in the <code>cucumber.runtime.java.spring.hooks</code> package.
This package isn't on your <a href="/api.html#glue-code">Glue Path</a> by default, so you have to add it yourself in your <a href="/api.html#configuration">Configuration Options</a>.

<h5>Using JUnit</h5>

{% highlight java %}
@RunWith(Cucumber.class)
@Cucumber.Options(glue = {"your.own.glue.code", "cucumber.runtime.java.spring.hooks"})
public class RunCukesTest {
}
{% endhighlight %}

<h5>Using the CLI</h5>

{% highlight text %}
--glue your.own.glue.code --glue cucumber.runtime.java.spring.hooks
{% endhighlight %}

See the <a href="https://github.com/cucumber/cucumber-jvm/tree/master/examples/spring-txn">spring-txn</a> example in Cucumber-JVM for a minimal setup.
  </div>
</div>

### Browsers, beware

If you're using a [Browser Automation](/browser-automation.html) tool that talks to your application over HTTP the transactional approach
will not work if your Step Definitions and the web application serving HTTP request each have their own database connection.

TODO: Write some more here.