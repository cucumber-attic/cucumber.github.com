---
layout: default
title: Cucumber-Ruby Installation
---
## {{page.title}}

Note: If you are using [Ruby on Rails](http://rubyonrails.org/), see [Cucumber-Rails Installation](/install-rails.html).

Cucumber-Ruby is a ruby gem, and can be installed from the command line:

<pre class="sh_sh"><code>{% capture code %}$ gem install cucumber
{% endcapture %}{{ code | xml_escape }}</code></pre>

If you are using [Bundler](http://gembundler.com/), just add it to your `Gemfile`:

<pre class="sh_ruby"><code>{% capture code %}group :test do
  gem 'cucumber'
end
{% endcapture %}{{ code | xml_escape }}</code></pre>
