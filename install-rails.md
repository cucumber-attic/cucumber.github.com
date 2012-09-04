---
layout: default
title: Cucumber-Rails Installation
---
## {{page.title}}

Before you can use the generator, add the gem to your project's Gemfile as follows:

{% highlight ruby %}
group :test do
  gem 'cucumber-rails', :require => false
  # database_cleaner is not required, but highly recommended
  gem 'database_cleaner'
end
{% endhighlight %}

Then install it by running:

{% highlight bash %}
bundle install
{% endhighlight %}

Learn about the various options:

{% highlight bash %}
rails generate cucumber:install --help
{% endhighlight %}

Finally, bootstrap your Rails app, for example:

{% highlight bash %}
rails generate cucumber:install
{% endhighlight %}

## Running Cucumber

With Rake:

{% highlight bash %}
rake cucumber
{% endhighlight %}

Without Rake:

{% highlight bash %}
[bundle exec] cucumber
{% endhighlight %}
