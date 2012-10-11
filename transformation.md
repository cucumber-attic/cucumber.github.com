---
layout: bootstrap
title: Transformation
---
## {{page.title}}

When Cucumber executes a [Step Definition](/step-definitions.html) it will pass arguments from capture groups and Doc Strings as strings by default. Tables will be passed as `DataTable` arguments by default.

Sometimes it can be convenient to tell Cucumber to _transform_ these arguments into a different type before executing the Step Definition.

### Transforming Strings

Consider the following Scenario. The `Given I have 48 cukes in my belly`. 

{% highlight gherkin %}
Scenario: Some cukes
  Given I have 48 cukes in my belly
{% endhighlight %}

#### Statically typed languages

With statically typed languages, transforming the arguments to a different type is easy. All you need to do is to declare each argument as the desired type and the transformation happens automatically:

<ul class="nav nav-tabs">
  <li><a href="#strings-cplusplus" data-toggle="tab" class="cplusplus"><div>&nbsp;</div></a></li>
  <li><a href="#strings-csharp" data-toggle="tab" class="csharp"><div>&nbsp;</div></a></li>
  <li><a href="#strings-fsharp" data-toggle="tab" class="fsharp"><div>&nbsp;</div></a></li>
  <li><a href="#strings-groovy" data-toggle="tab" class="groovy"><div>&nbsp;</div></a></li>
  <li><a href="#strings-java" data-toggle="tab" class="java"><div>&nbsp;</div></a></li>
  <li><a href="#strings-scala" data-toggle="tab" class="scala"><div>&nbsp;</div></a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane" id="strings-cplusplus">
{% highlight cpp %}
GIVEN("^I have (\\d+) cukes in my belly$") {
    REGEX_PARAM(int, cukes);
    // Do something with the cukes
}
{% endhighlight %}
  </div>
  <div class="tab-pane" id="strings-csharp">
{% highlight csharp %}
[When(@"^I have (\d+) cukes in my belly$")]
public void CukesInTheBelly(int cukes)
{
    // Do something with the cukes
}
{% endhighlight %}
  </div>
  <div class="tab-pane" id="strings-fsharp">
{% highlight fsharp %}
let [<Given>] ``^I have (\d+) cukes in my belly$``(cukes:int) = 
  (* Do something with the cukes *)
{% endhighlight %}
  </div>
  <div class="tab-pane" id="strings-groovy">
{% highlight groovy %}
Given(~'^I have (\\d+) cukes in my belly') { int cukes ->
    // Do something with the cukes
}
{% endhighlight %}
  </div>
  <div class="tab-pane" id="strings-java">
{% highlight java %}
@Given("I have (\\d+) cukes in my belly")
public void cukesInTheBelly(int cukes) {
    // Do something with the cukes
}
{% endhighlight %}
  </div>
  <div class="tab-pane" id="strings-scala">
{% highlight scala %}
Given("""^I have (\d+) cukes in my belly$"""){ (cukes:Int) =>
  // Do something with the cukes
}
{% endhighlight %}
  </div>
</div>

### Transforming Data Tables

Data Tables can be transformed to a rich set of types.

Consider the following Scenario. The `Given I have 48 cukes in my belly`. 

{% highlight gherkin %}
Scenario: Some vegetables
  Given I have these vegetables:
    | name     | color |
    | Cucumber | Green |
    | Tomato   | Red   |
{% endhighlight %}

This table can be transformed into a list of vegetables:

{% highlight java %}
public class Vegetable {
    public String name;
    public Color color; // Color is an enum
}
{% endhighlight %}

The Step Definition:

{% highlight java %}
@Given("I have these vegetables:")
public void I_have_these_vegetables(List<Vegetable> vegetables) {
    // Do something with the vegetables
}
{% endhighlight %}

The header row is used to name fields in the generic List type (or Map keys - see below). If the generic List type (`Vegetable` in this case) has a String constructor (see [Single value types](#single_value_types) below) the header row will not have a special meaning, and the 

You can also transform it to a list of maps:

{% highlight java %}
@Given("I have these vegetables:")
public void I_have_these_vegetables(List<Map<String, String> vegetables) {
    // Do something with the vegetables
}
{% endhighlight %}

The `Key` and `Value` generic types of the `Map` can be any kind of "single value" (enum, String, Integer etc).

You can also convert it to a list of list "single values":

{% highlight java %}
@Given("I have these vegetables:")
public void I_have_these_vegetables(List<List<String>> vegetables) {
    // Do something with the vegetables
}
{% endhighlight %}

This will convert it to a flattened list like this: `[["name", "color"], ["Cucumber", "Green"], ["Tomato", "Red"]]`
You can also convert it to a list of "single values":

{% highlight java %}
@Given("I have these vegetables:")
public void I_have_these_vegetables(List<String> vegetables) {
    // Do something with the vegetables
}
{% endhighlight %}

This will convert it to a flattened list like this: `["name", "color", "Cucumber", "Green", "Tomato", "Red"]`

#### Single value types

A single value type is a type that can be converted from a single string:

* Subclass of Number
   * Byte
   * Double
   * Float
   * Integer
   * Long
   * Short
* BigDecimal
* BigInteger
* Calendar
* Date
* enum
* Any Class with a String constructor
* A generic List of any of the above types
