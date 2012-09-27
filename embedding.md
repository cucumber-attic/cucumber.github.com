---
layout: default
title: Embedding
---
## {{page.title}}

If you are using Cucumber with a GUI driver such as a [Browser Automation](/browser-automation.html) tool,
it can sometimes be useful to embed screenshots or videos of the user interface in Cucumber's [HTML](/reports.html#HTML) or [JSON](/reports.html#JSON) report.

Cucumber itself doesn't provide an API to _take_ screenshots or videos, but it provides an API to _embed_ them
into the report. For example, if you are using Selenium WebDriver, you can ask it to give you a screenshot, and
then embed them into the report.

{% highlight java %}
@After
public void embedScreenshot(ScenarioResult result) {
    if(result.isFailed()) {
        byte[] screenshot = webDriver.getScreenshotAs(OutputType.BYTES);
        result.embed(screenshot, "image/png");
    }
}
{% endhighlight %}
