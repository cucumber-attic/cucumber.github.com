---
layout: default
title: Step Definitions
---
## {{page.title}}

A Step Definition is a small piece of _code_ with a _pattern_ attached to it. The pattern is used to link the step definition to all the matching [Gherkin Steps](/gherkin.html#steps), and the _code_ is what Cucumber will execute when it sees a Gherkin Step.

<ul>
  <li>Ruby
    <pre class="sh_ruby"><code>{% capture code %}Given(/I have (\d+) cukes in my belly/) do |cukes|
end{% endcapture %}{{ code | xml_escape }}</code></pre>
  </li>
  <li>Java
    <pre class="sh_java"><code>{% capture code %}@Given("I have (\\d+) cukes in my belly")
public void cukesInTheBelly(int cukes) {
}{% endcapture %}{{ code | xml_escape }}</code></pre>
  </li>
</ul>