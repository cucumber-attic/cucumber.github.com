---
layout: bootstrap
title: Install Cucumber-Ruby
---
# {{page.title}}

Note: If you are using [Ruby on Rails](http://rubyonrails.org/), see [Install Cucumber-Rails](/install-cucumber-rails.html).

Cucumber-Ruby is a ruby gem, and can be installed from the command line:

{% highlight text %}
gem install cucumber
{% endhighlight %}

If you are using [Bundler](http://gembundler.com/), just add it to your `Gemfile`:

{% highlight ruby %}
group :test do
  gem 'cucumber'
end
{% endhighlight %}
