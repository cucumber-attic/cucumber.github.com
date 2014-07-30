---
layout: bootstrap
title: Step Definitions
---
# {{page.title}}

*TODO* Migrate docs from https://github.com/cucumber/cucumber/wiki/Step-Definitions, especially states (successful, undefined etc.)

When Cucumber executes a [Step](/gherkin.html#steps) in a [Scenario](/gherkin.html#scenario) it will look for a matching _Step Definition_ to execute.

A Step Definition is a small piece of _code_ with a _pattern_ attached to it. The pattern is used to link the step definition to all the matching [Steps](/gherkin.html#steps), and the _code_ is what Cucumber will execute when it sees a Gherkin Step.

Step Definitions sources must be placed in a file where Cucumber can find them. The location depends on what Cucumber implementation you are using. See [Glue Code](/glue-code.html) for details.

To understand how Step Definitions work, consider the following Scenario:

{% highlight gherkin %}
Scenario: Some cukes
  Given I have 48 cukes in my belly
{% endhighlight %}

The `I have 48 cukes in my belly` part of the step (the text following the `Given` keyword) will match the Step Definition below.

<ul class="nav nav-tabs">
  <li><a href="#defs-java" data-toggle="tab" class="java"><div>&nbsp;</div></a></li>
  <li><a href="#defs-ruby" data-toggle="tab" class="ruby"><div>&nbsp;</div></a></li>
  <li><a href="#defs-groovy" data-toggle="tab" class="groovy"><div>&nbsp;</div></a></li>
  <li><a href="#defs-js" data-toggle="tab" class="js"><div>&nbsp;</div></a></li>
  <li><a href="#defs-clojure" data-toggle="tab" class="clojure"><div>&nbsp;</div></a></li>
  <li><a href="#defs-cplusplus" data-toggle="tab" class="cplusplus"><div>&nbsp;</div></a></li>
  <li><a href="#defs-lua" data-toggle="tab" class="lua"><div>&nbsp;</div></a></li>
  <li><a href="#defs-python" data-toggle="tab" class="python"><div>&nbsp;</div></a></li>
  <li><a href="#defs-scala" data-toggle="tab" class="scala"><div>&nbsp;</div></a></li>
  <li><a href="#defs-csharp" data-toggle="tab" class="csharp"><div>&nbsp;</div></a></li>
  <li><a href="#defs-fsharp" data-toggle="tab" class="fsharp"><div>&nbsp;</div></a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane" id="defs-java">
{% highlight java %}
@Given("I have (\\d+) cukes in my belly")
public void I_have_cukes_in_my_belly(int cukes) {
    // Do something with the cukes
}
{% endhighlight %}

<p>
Lists can also be specified:
</p>

{% highlight gherkin %}
Given I am available on "Tuesday,Friday,Sunday"
{% endhighlight %}

{% highlight java %}
@Given("I am available on \"(.+)\"")
public void I_am_available_on(List<String> days) {
    // Do something with the days
}
{% endhighlight %}
  </div>
  <div class="tab-pane" id="defs-ruby">
{% highlight ruby %}
Given(/I have (\d+) cukes in my belly/) do |cukes|
  # Do something with the cukes
end
{% endhighlight %}
  </div>
  <div class="tab-pane" id="defs-groovy">
{% highlight groovy %}
Given(~'^I have (\\d+) cukes in my belly') { int cukes ->
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
  <div class="tab-pane" id="defs-clojure">
{% highlight clojure %}
(Given #"^I have (\d+) cukes in my belly$" [cukes]
  (eat (Integer. cukes)))
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
  (* Do something with the cukes *)
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
  <div class="tab-pane" id="defs-scala">
{% highlight scala %}
Given("""^I have (\d+) cukes in my belly$"""){ (cukes:Int) =>
  // Do something with the cukes
}
{% endhighlight %}
  </div>
</div>

When Cucumber matches a Step against a regular expression in a Step Definition, it passes the value of all the capture groups to the Step Definition's arguments. Capture groups are strings (even when they match digits like `\d+`). For statically typed languages,
Cucumber will automatically transform those strings into the appropriate type. For dynamically typed languages, no transformation happens by default, as there is no type information.

Cucumber does not differentiate between `Given`, `When` and `Then`. It is up to you what you do inside the Step Definition's body.

## Doc Strings

Doc Strings are handy for specifying a larger piece of text. This is inspired from Python's [Docstring](http://www.python.org/dev/peps/pep-0257/) syntax.

The text should be offset by delimiters consisting of three double-quote marks on lines of their own:

{% highlight gherkin %}
Given a blog post named "Random" with Markdown body
  """
  Some Title, Eh?
  ==============
  Here is the first paragraph of my blog post. Lorem ipsum dolor sit amet,
  consectetur adipiscing elit.
  """
{% endhighlight %}

In your step definition, there’s no need to find this text and match it in your Regexp. It will automatically be passed as the last parameter in the step definition. For example:

<ul class="nav nav-tabs">
  <li><a href="#docstrings-java" data-toggle="tab" class="java"><div>&nbsp;</div></a></li>
  <li><a href="#docstrings-ruby" data-toggle="tab" class="ruby"><div>&nbsp;</div></a></li>
</ul>

<div class="tab-content">
  <div class="tab-pane" id="docstrings-java">
{% highlight java %}
@Given("^a blog post named \"([^\"]*)\" with Markdown body$")
public void a_blog_post_named_something_with_markdown_body(String title, String markdown) {
    // Save it in the database
}
{% endhighlight %}
  </div>

  <div class="tab-pane" id="docstrings-ruby">
{% highlight ruby %}
Given /^a blog post named "([^"]*)" with Markdown body$/ do |title, markdown|
  Post.create!(:title => title, :body => markdown)
end
{% endhighlight %}
  </div>
</div>

Indentation of the opening `"""` is unimportant, although common practice is two spaces in from the enclosing step. The indentation inside the triple quotes, however, _is_ significant. Each line of the string passed to the step definition’s block will be de-indented according to the opening `"""`. Indentation beyond the column of the opening `"""` will therefore be preserved.

## Data Tables

Data Tables are handy for specifying a larger piece of data:

{% highlight gherkin %}
Given the following users exist:
  | name  | email           | phone |
  | Aslak | aslak@email.com | 123   |
  | Matt  | matt@email.com  | 234   |
  | Joe   | joe@email.org   | 456   |
{% endhighlight %}

Just like Doc Strings, they will be passed to the Step Definition as the last argument:

<ul class="nav nav-tabs">
  <li><a href="#datatables-java" data-toggle="tab" class="java"><div>&nbsp;</div></a></li>
  <li><a href="#datatables-ruby" data-toggle="tab" class="ruby"><div>&nbsp;</div></a></li>
</ul>

<div class="tab-content">
  <div class="tab-pane" id="datatables-java">
{% highlight java %}
@Given("^the following users exist$")
public void the_following_users_exist(DataTable users) {
    // Save them in the database
}
{% endhighlight %}

    See the <a href="/api/cucumber/ruby/yardoc/Cucumber/Ast/Table.html">DataTable</a>
    API docs for details about how to access data in the table.
  </div>

  <div class="tab-pane" id="datatables-ruby">
{% highlight ruby %}
Given /^the following users exist$/ do |users|
  User.create!(users.hashes)
end
{% endhighlight %}

    See the <a href="/api/cucumber/ruby/yardoc/Cucumber/Ast/Table.html">DataTable</a>
    API docs for details about how to access data in the table.
  </div>
</div>

### Substitution in Scenario Outlines

If you use a DocString or DataTable argument in steps in [Scenario Outlines](/gherkin.html#scenario_outlines), any `< >`
delimited tokens will be substituted with values from the example tables. For example:

{% highlight gherkin %}
Scenario Outline: Email confirmation
  Given I have a user account with my name "Jojo Binks"
  When an Admin grants me <Role> rights
  Then I should receive an email with the body:
    """
    Dear Jojo Binks,
    You have been granted <Role> rights.  You are <details>. Please be responsible.
    -The Admins
    """
  Examples:
    |  Role     | details                                         |
    |  Manager  | now able to manage your employee accounts       |
    |  Admin    | able to manage any user account on the system   |
{% endhighlight %}

### Data Table diffing

One very powerful feature in Cucumber is comparison of tables. You can compare a table argument to another table that you provide within your step definition. This is something you would typically do in a `Then` step, and the other table would typically be constructed programmatically from your application’s data.

Beware that the diffing algorithm expects your data to be column-oriented, and that the first row of both tables represents column names. If your tables don’t have some similarity in the first row you will not get very useful results. The column names must be unique for each column – and they must match.

Here is an example of a Data Table that we want to diff against actual results:

{% highlight gherkin %}
Then I should see the following cukes:
  | Latin           | English      |
  | Cucumis sativus | Cucumber     |
  | Cucumis anguria | Burr Gherkin |
{% endhighlight %}

A Step Definition can diff the DataTable with data pulled out of your application, for example from a Web page or a Database:

<ul class="nav nav-tabs">
  <li><a href="#diff-java" data-toggle="tab" class="java"><div>&nbsp;</div></a></li>
  <li><a href="#diff-ruby" data-toggle="tab" class="ruby"><div>&nbsp;</div></a></li>
</ul>

<div class="tab-content">
  <div class="tab-pane" id="diff-java">
{% highlight java %}
@Then("^I should see the following cukes:$")
public void the_following_users_exist(DataTable expectedCukesTable) {
    // We'd typically pull this out of a database or a web page...
    List<Cuke> actualCukes = new ArrayList();
    actualCukes.add(new Cuke("Cucumis sativus", "Concombre"));
    actualCukes.add(new Cuke("Cucumis anguria", "Burr Gherkin"));

    expectedCukesTable.diff(actualCukes)
}
{% endhighlight %}

    <p>
      The list passed to <code>diff</code> can be a <code>DataTable</code>, <code>List&lt;YourType&gt;</code>,
      <code>List&lt;Map&gt;</code> or a <code>List&lt;List&lt;ScalarType&gt;&gt;</code>.
    </p>
  </div>
  <div class="tab-pane" id="diff-ruby">
{% highlight ruby %}
Then /^I should see the following cukes:$/ do |expected_cukes_table|
  # We'd typically pull this out of a database or a web page...
  actual_cukes = [
    ['Latin', 'English'],
    ['Cucumis sativus', 'Concombre'],
    ['Cucumis anguria', 'Burr Gherkin']
  ]

  expected_cukes_table.diff!(actual_cukes)
end
{% endhighlight %}

    <p>
      The list passed to <code>diff!</code> can be a <code>Cucumber::Ast::Table</code>,
      <code>Array</code> of <code>Map</code> or an <code>Array</code> of <code>Array</code> of <code>String</code>.
    </p>

    <p>
      If you are using [Capybara](http://jnicklas.github.com/capybara/) and you want to compare a Gherkin DataTable with a
      HTML table rendered in a Web page you can construct an Array like so:
    </p>

{% highlight ruby %}
rows = find("table#selector").all('tr')
table = rows.map { |r| r.all('th,td').map { |c| c.text.strip } }
expected_table.diff!(table)
{% endhighlight %}
  </div>
</div>

If the tables are different, an exception is thrown, and the diff of the two tables are reported in the [Report](/reports.html).

## String Transformations

Cucumber provides an API that lets you take control over how strings are converted to other types. This is useful especially for dynamically typed languages, but also for statically typed languages when you need more control over the transformation.

Let's consider a common example - turning a string into a date:

{% highlight gherkin %}
Given today's date is "10-03-1971"
{% endhighlight %}

First of all, this might mean the 10th of March in some countries, and the 3rd of October in others. It's best to be explicit about how we want this converted. We'll try to convert it to _10th of March 1971_.

<ul class="nav nav-tabs">
  <li><a href="#transform-java" data-toggle="tab" class="java"><div>&nbsp;</div></a></li>
  <li><a href="#transform-ruby" data-toggle="tab" class="ruby"><div>&nbsp;</div></a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane" id="transform-java">
    <p>
    Cucumber-JVM knows how to convert strings into various <em>scalar</em> types. A scalar type is a type that can be derived from a single
    string value. Cucumber-JVM's built-in scalar types are <em>numbers</em>, <em>enums</em>, <code>java.util.Date</code>,
    <code>java.util.Calendar</code> and arbitrary types that have a single-argument constructor that is either a
    <code>String</code> or an <code>Object</code>.
    </p>

    <p>
    Transformation to <code>java.util.Date</code> and <code>java.util.Calendar</code> will work out-of-the-box as long as the
    string value matches one of the <code>SHORT</code>, <code>MEDIUM</code>, <code>FULL</code> or <code>LONG</code> formats
    defined by <a href="http://docs.oracle.com/javase/7/docs/api/java/text/DateFormat.html"><code>java.util.DateFormat</code></a>.
    </p>

    <p>
    It turns out that <code>10-03-1971</code> from our example doesn't match any of those formats, so we have to give Cucumber a hint:
    </p>

{% highlight java %}
@Given("today's date is \"(.*)\"")
public void todays_date_is(@Format("dd-MM-yyyy") Date today) {
}
{% endhighlight %}

    <p>
    Many Java programmers like to use <a href="http://joda-time.sourceforge.net/">Joda Time</a>. Cucumber-JVM doesn't have any special support for Joda Time, but since Joda's <code>LocalDate</code> has a <code>LocalDate(Object)</code> constructor it is considered a scalar by default.
    </p>

    <p>
    However, in this case it wouldn't also know how to pass the _format_ string, so you would get an exception when Cucumber instantiates it
    with <code>new LocalDate("10-03-1971")</code>.
    </p>

    <p>
    A custom formatter gives you full control:
    </p>

{% highlight java %}
@Given("today's date is \"(.*)\"")
public void todays_date_is(
  @Format("dd-MM-yyyy")
  @Transform(JodaTransformer.class)
  LocalDate today) {
}
{% endhighlight %}

    <p>
    The custom transformer looks like this:
    </p>

{% highlight java %}
public class JodaTransformer extends Transformer<LocalDate> {
    @Override
    public LocalDate transform(String value) {
        String format = getParameterInfo().getFormat();
        DateTimeFormatter dateTimeFormatter = DateTimeFormat.forStyle(format);
        dateTimeFormatter = dateTimeFormatter.withLocale(getLocale());
        return dateTimeFormatter.parseLocalDate(value);
    }
}
{% endhighlight %}

    <p>
    Of course, you can write transformers for anything, not just dates.
    </p>

  </div>
  <div class="tab-pane" id="transform-ruby">
    <p>
    Let's <code>Transform</code> anything that looks like a date into an instance of <code>Date</code>:

{% highlight ruby %}
require 'date'

Transform(/^(\d\d-\d\d-\d\d\d\d)$/) do |arg|
  Date.strptime(arg, '%d-%m-%Y')
end
{% endhighlight %}
    </p>
  </div>
</div>

## Data Table Transformations

*This applies to Cucumber-JVM only*

Data Tables can be transformed to a `List` of various types.
We'll see how the table in the following Scenario can be transformed to different kinds of lists.

{% highlight gherkin %}
Scenario: Some vegetables
  Given I have these vegetables:
    | name     | color |
    | Cucumber | Green |
    | Tomato   | Red   |
{% endhighlight %}

### List of YourType

The table can be transformed into a list of vegetables:

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

The header row is used to name fields in the generic List type.

*IMPORTANT*: If the generic List type (`Vegetable` in this case) is a <em>scalar</em> (i.e. it has a `String` or `Object` constructor),
the header will *not* be used to name fields in the class. Instead you would get a List that has one `Vegetable` for *each cell*
(6 in this case). See [List of Scalar](#list_of_scalar) below.

### List of Map

You can also transform a DataTable to a list of maps:

{% highlight java %}
@Given("I have these vegetables:")
public void I_have_these_vegetables(List<Map<String, String>> vegetables) {
    // Do something with the vegetables
}
{% endhighlight %}

The `Key` and `Value` generic types of the `Map` can be any kind of scalar type.

### List of List of scalar

You can also convert it to a list of list scalar:

{% highlight java %}
@Given("I have these vegetables:")
public void I_have_these_vegetables(List<List<String>> vegetables) {
    // Do something with the vegetables
}
{% endhighlight %}

This will convert it to a flattened list like this:

`[["name", "color"], ["Cucumber", "Green"], ["Tomato", "Red"]]`

You can also convert it to a list of scalar:

### List of scalar

{% highlight java %}
@Given("I have these vegetables:")
public void I_have_these_vegetables(List<String> vegetables) {
    // Do something with the vegetables
}
{% endhighlight %}

This will convert it to a flattened list like this: `["name", "color", "Cucumber", "Green", "Tomato", "Red"]`

### Map of scalar

{% highlight java %}
@Given("I have these vegetables:")
public void I_have_these_vegetables(Map<String,String> vegetables) {
    // Do something with the vegetables
}
{% endhighlight %}

This will convert it to a map list like this: `{"name" => "color", "Cucumber" => "Green", "Tomato" => "Red"}`

Note that this only works for tables with 2 columns. If you're converting into a `Map`
it is usually adviseable that the Gherkin table doesn't have a top row naming the columns.

## FAQ

### I want to scope a step definition to a scenario or feature

TODO: Summarise info from:

* https://groups.google.com/d/msg/cukes/53UKauIY28o/1nrdSCWAkLMJ
* https://github.com/cucumber/cucumber/wiki/Feature-Coupled-Step-Definitions-(Antipattern)
