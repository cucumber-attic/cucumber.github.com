---
layout: bootstrap
title: Dependency Injection
---
# {{page.title}}

_This is only relevant if you are using Cucumber-JVM with Java_.

Java Step Definitions are annotated methods that live in a class:

{% highlight java %}
public class BellyStepdefs {
    @Given("I have (\\d+) cukes in my belly")
    public void cukesInTheBelly(int cukes) {
        // Do something with the cukes
    }
}
{% endhighlight %}

For each scenario, Cucumber will instantiate all classes that have _glue code_ ([Step Definitions](/step-definitions.html) or [Hooks](/hooks.html)).

## TODO

* Describe why inheritance is bad
* DI allows glue classes to share references to the same instances
* Describe the different containers
* Check the mailing list for common Q&A
