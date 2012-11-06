---
layout: bootstrap
title: Formatting
---
# {{page.title}}

TODO: Move over content from https://github.com/cucumber/cucumber/wiki/Custom-Formatters

## Custom formatters

You can write a custom formatter for Cucumber-JVM by implementing `gherkin.formatter.Formatter` and optionally `gherkin.formatter.Reporter`. Example:

{% highlight java %}
package foo;

public class BarFormatter implements gherkin.formatter.Formatter {
    // Implement the interface(s)
}
{% endhighlight %}

Now you can specify this formatter from the command line:

{% highlight text %}
--format foo.BarFormatter
{% endhighlight %}

