---
layout: bootstrap
title: Encoding
---
# {{page.title}}

By default, `.feature` files are in English, with `UTF-8` encoding. You can override this if you want:

{% highlight gherkin %}
# language: fr
Fonctionnalité: Concombres
  Scénario: dans le bide
    Étant donné j'ai 5 concombres dans mon bide
{% endhighlight %}

If you wish to use a different encoding than `UTF-8`, you can add another header:

{% highlight gherkin %}
# language: fr
# encoding: ISO-8859-1
Fonctionnalité: Concombres
  Scénario: dans le bide
    Étant donné j'ai 5 concombres dans mon bide
{% endhighlight %}
