---
layout: bootstrap
title: Install Cucumber-Rails
---
# {{page.title}}

Cucumber-Rails is a generator that will generate and modify files in a Rails project so it can be used with Cucumber.
Before you can use the generator, add the gem to your project's Gemfile as follows:

{% highlight ruby %}
group :test, :development do
  gem 'cucumber-rails', :require => false
  # database_cleaner is not required, but highly recommended
  gem 'database_cleaner'
end
{% endhighlight %}

Then install it by running:

{% highlight text %}
bundle install
{% endhighlight %}

Learn about the various options:

{% highlight text %}
cucumber --help
{% endhighlight %}

Finally, bootstrap your Rails app, for example:

{% highlight text %}
rails generate cucumber:install
{% endhighlight %}

## Running Cucumber

With Rake:

{% highlight text %}
rake cucumber
{% endhighlight %}

Without Rake:

{% highlight text %}
[bundle exec] cucumber
{% endhighlight %}
