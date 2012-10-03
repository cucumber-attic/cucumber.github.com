---
layout: bootstrap
title: Cucumber-Rails Installation
---
## {{page.title}}

Before you can use the generator, add the gem to your project's Gemfile as follows:

<pre class="sh_ruby"><code>{% capture code %}group :test do
  gem 'cucumber-rails', :require => false
  # database_cleaner is not required, but highly recommended
  gem 'database_cleaner'
end
{% endcapture %}{{ code | xml_escape }}</code></pre>

Then install it by running:

<pre class="sh_sh"><code>{% capture code %}bundle install
{% endcapture %}{{ code | xml_escape }}</code></pre>

Learn about the various options:

<pre class="sh_sh"><code>{% capture code %}rails generate cucumber:install --help
{% endcapture %}{{ code | xml_escape }}</code></pre>

Finally, bootstrap your Rails app, for example:

<pre class="sh_sh"><code>{% capture code %}rails generate cucumber:install
{% endcapture %}{{ code | xml_escape }}</code></pre>

## Running Cucumber

With Rake:

<pre class="sh_sh"><code>{% capture code %}rake cucumber
{% endcapture %}{{ code | xml_escape }}</code></pre>

Without Rake:

<pre class="sh_sh"><code>{% capture code %}[bundle exec] cucumber
{% endcapture %}{{ code | xml_escape }}</code></pre>
