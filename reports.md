---
layout: bootstrap
title: Cucumber Reports
---
# {{page.title}}

Cucumber can report results in several different formats, using _formatters_. Formatters are specified either on the command line or in code. Some formatters generate files while others print to `STDOUT`. You can specify as many formatters as you like.

The available formatters are:

#### Pretty

Prints the [gherkin](/gherkin.html) source with additional colours and stack traces for errors

#### HTML

This report is handy for publishing

#### JSON

This report contains all the information from the [gherkin](/gherkin.html) source, with additional results for each step, including embedded screenshots. This report is meant to be post-processed into another visual format by 3rd party tools such as [Cucumber Jenkins](https://github.com/masterthought/jenkins-cucumber-jvm-reports-plugin).

#### Progress

This report prints results to `STDOUT`, on character at a time. It looks like this:

<pre><code>....F--U.......</code></pre>

#### Usage

This report prints statistics to `STDOUT`. Programmers may find it useful to find slow or unused [Step Definitions](/step-definitions.html).

#### JUnit

This report generates XML files just like [Apache Ant](http://ant.apache.org/)'s [junitreport](https://ant.apache.org/manual/Tasks/junitreport.html) task. This XML format is understood by most [Continuous Integration](http://en.wikipedia.org/wiki/Continuous_integration) servers, who will use it to generate visual reports.

#### Rerun

This report generates a file that lists the location of failed Scenarios. This can be picked up by subsequent Cucumber runs, allowing only previously failed Scenarios to be rerun. Programmers may find this useful while fixing broken scenarios, especially if running all scenarios is time-consuming.

### Embedding extra information in reports

Programmers can embed text and images into reports via an API that is available in [Step Definitions](/step-definitions.html) and [Hooks](/hooks.html). This can make it easier to diagnose failures. Some reports will ignore embedded data while others will include it.

#### Embedding Text

Text is embedded in the following way:

<ul class="nav nav-tabs">
  <li><a href="#text-ruby" data-toggle="tab" class="ruby"><div>&nbsp;</div></a></li>
  <li><a href="#text-java" data-toggle="tab" class="java"><div>&nbsp;</div></a></li>
</ul>

<div class="tab-content">
  <div class="tab-pane" id="text-ruby">
{% highlight ruby %}
When /I do the deed/ do
  puts 'This goes into the report'
  Kernel.puts 'This goes to STDOUT, but not into the report'
end
{% endhighlight %}
  </div>

  <div class="tab-pane" id="text-java">
{% highlight java %}
@Before
public void before(Scenario scenario) {
    this.scenario = scenario;
}

@When("I do the deed")
public void do_the_deed() {
    scenario.write("This goes into the report");
    System.out.println("This goes to STDOUT, but not into the report");
}
{% endhighlight %}
  </div>
</div>

#### Embedding Screenshots

TODO: Add an image of a report with a screenshot. Can be a close-up with a small section.

If you are using Cucumber with a GUI driver such as a [Browser Automation](/browser-automation.html) tool,
it can sometimes be useful to embed screenshots or videos of the user interface in Cucumber's [HTML](/reports.html#html) or [JSON](/reports.html#json) report.

Cucumber itself doesn't provide an API to _take_ screenshots or videos, but it provides an API to _embed_ them
into the report. For example, if you are using [Selenium WebDriver](http://seleniumhq.org/projects/webdriver/), 
you can ask it to give you a screenshot, and then embed them into the report.

<ul class="nav nav-tabs">
  <li><a href="#screenshots-ruby" data-toggle="tab" class="ruby"><div>&nbsp;</div></a></li>
  <li><a href="#screenshots-java" data-toggle="tab" class="java"><div>&nbsp;</div></a></li>
</ul>

<div class="tab-content">
  <div class="tab-pane" id="screenshots-ruby">
{% highlight ruby %}
After do |scenario|
  if(scenario.failed?)
    page.driver.browser.save_screenshot("html-report/#{scenario.__id__}.png")
    embed("#{scenario.__id__}.png", "image/png", "SCREENSHOT")
  end
end
{% endhighlight %}
  </div>
  <div class="tab-pane" id="screenshots-java">
{% highlight java %}
@After
public void embedScreenshot(Scenario scenario) {
    if(result.isFailed()) {
        byte[] screenshot = webDriver.getScreenshotAs(OutputType.BYTES);
        scenario.embed(screenshot, "image/png");
    }
}
{% endhighlight %}
  </div>
</div>