---
layout: bootstrap
title: Step Definitions
---
## {{page.title}}

When Cucumber executes a [Step](/gherkin.html#steps) in a [Scenario](/gherkin.html#scenario) it will look for a matching _Step Definition_ to execute.

A Step Definition is a small piece of _code_ with a _pattern_ attached to it. The pattern is used to link the step definition to all the matching [Steps](/gherkin.html#steps), and the _code_ is what Cucumber will execute when it sees a Gherkin Step.

Consider the following Scenario. The `Given I have 48 cukes in my belly` step will match the Step Definition below. 

{% highlight gherkin %}
Scenario: Some cukes
  Given I have 48 cukes in my belly
{% endhighlight %}

<ul class="nav nav-tabs">
  <li><a href="#defs-clojure" data-toggle="tab" class="clojure"><div>&nbsp;</div></a></li>
  <li><a href="#defs-cplusplus" data-toggle="tab" class="cplusplus"><div>&nbsp;</div></a></li>
  <li><a href="#defs-csharp" data-toggle="tab" class="csharp"><div>&nbsp;</div></a></li>
  <li><a href="#defs-fsharp" data-toggle="tab" class="fsharp"><div>&nbsp;</div></a></li>
  <li><a href="#defs-groovy" data-toggle="tab" class="groovy"><div>&nbsp;</div></a></li>
  <li><a href="#defs-java" data-toggle="tab" class="java"><div>&nbsp;</div></a></li>
  <li><a href="#defs-js" data-toggle="tab" class="js"><div>&nbsp;</div></a></li>
  <li><a href="#defs-lua" data-toggle="tab" class="lua"><div>&nbsp;</div></a></li>
  <li><a href="#defs-python" data-toggle="tab" class="python"><div>&nbsp;</div></a></li>
  <li><a href="#defs-ruby" data-toggle="tab" class="ruby"><div>&nbsp;</div></a></li>
  <li><a href="#defs-scala" data-toggle="tab" class="scala"><div>&nbsp;</div></a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane" id="defs-clojure">
{% highlight clojure %}
(Given #"^I have (\d+) cukes in my belly$" [cukes]
  (eat (Float. cuke-count)))
{% endhighlight %}
  </div>
  <div class="tab-pane" id="defs-cplusplus">
{% highlight cpp %}
GIVEN("^I have (\\d+) cukes in my belly$") {
    REGEX_PARAM(int, cukes);
    USING_CONTEXT(MyAppCtx, context);
    // Do something with the cukes
}
{% endhighlight %}
  </div>
  <div class="tab-pane" id="defs-csharp">
{% highlight csharp %}
[When(@"^I have (\d+) cukes in my belly$")]
public void CukesInTheBelly(int cukes)
{
    // Do something with the cukes
}
{% endhighlight %}
  </div>
  <div class="tab-pane" id="defs-fsharp">
{% highlight fsharp %}
let [<Given>] ``^I have (\d+) cukes in my belly$``(cukes:int) = 
  Belly.Push(cukes)
{% endhighlight %}
  </div>
  <div class="tab-pane" id="defs-groovy">
{% highlight groovy %}
Given(~'^I have (\\d+) cukes in my belly') { int cukes ->
    // Do something with the cukes
}
{% endhighlight %}
  </div>
  <div class="tab-pane" id="defs-java">
{% highlight java %}
@Given("I have (\\d+) cukes in my belly")
public void cukesInTheBelly(int cukes) {
    // Do something with the cukes
}
{% endhighlight %}
  </div>
  <div class="tab-pane" id="defs-js">
{% highlight js %}
Given(/^I have (\d+) cukes in my belly$/, function (cukes) {
    // Do something with the cukes
});
{% endhighlight %}
  </div>
  <div class="tab-pane" id="defs-lua">
{% highlight lua %}
Given("^I have (%d+) cukes in my belly$", function (cukes)
    -- Do something with the cukes
end)
{% endhighlight %}
  </div>
  <div class="tab-pane" id="defs-python">
{% highlight python %}
@Given('^I have (\d+) cukes in my belly$')
def I_have_cukes_in_my_belly(self, cukes):
  # Do something with the cukes
  pass
{% endhighlight %}
  </div>
  <div class="tab-pane" id="defs-ruby">
{% highlight ruby %}
Given(/I have (\d+) cukes in my belly/) do |cukes|
  # Do something with the cukes
end
{% endhighlight %}
  </div>
  <div class="tab-pane" id="defs-scala">
{% highlight fsharp %}
Given("""^I have (\d+) cukes in my belly$"""){ (cukes:Int) =>
  // Do something with the cukes
}
{% endhighlight %}
  </div>
</div>

Cucumber will pass the values of the [Capture Arguments](#) to the Step Definition's code as arguments.

It is up to you what you do with those arguments. You can use it to interact with a Web Page using a [Browser Automation Tool](#) or you can invoke methods/functions directly in your application code.

## Doc Strings

## Data Tables

## Transformations

