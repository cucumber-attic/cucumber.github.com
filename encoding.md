---
layout: bootstrap
title: Encoding
---
## {{page.title}}

By default, `.feature` files are in English, with `UTF-8` encoding. You can override this if you want:

{% highlight gherkin %}
# language: fr
Fonctionnalité: Quelque chose
{% endhighlight %}

If you wish to use a different encoding than `UTF-8`, you can add another header:

{% highlight gherkin %}
# language: fr
# encoding: ISO-8859-1
Fonctionnalité: Quelque chose
{% endhighlight %}
