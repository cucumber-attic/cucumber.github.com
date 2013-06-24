---
layout: bootstrap
title: Browser Automation
---
# {{page.title}}
###Cucumber is _not_ a Browser Automation tool, but it _works well_ with Browser Automation tools such as [Selenium Webdriver](http://docs.seleniumhq.org/projects/webdriver/)
To illustrate this, let's convert the [Selenium-Webdriver by Example tutorial](http://docs.seleniumhq.org/docs/03_webdriver.jsp#introducing-the-selenium-webdriver-api-by-example) to use Cucumber.

We can express the example as the following Scenario:
{% highlight gherkin %}
Scenario: Page title should show search term
	Given I visit Google
	When I search for Cheese!
	Then the page title starts with cheese
{% endhighlight %}

Here are the accompanying Step Definitions:

<ul class="nav nav-tabs">
  <li><a href="#defs-java" data-toggle="tab" class="java"><div>&nbsp;</div></a></li>
</ul>

<div class="tab-content">
  <div class="tab-pane" id="defs-java">
{% highlight java %}
package com.example;

public class ExampleSteps {
    private WebDriver driver;

    @Before
    public void setup() {
        // Create a new instance of the Firefox driver
        // Notice that the remainder of the code relies on the interface,
        // not the implementation.
        driver = new FirefoxDriver();
    }

    @Given("^I visit Google$")
    public void I_visit_google() {
        driver.get("http://www.google.com");
    }

    @When("^I search for Cheese!$")
    public void search_for_cheese() {
        WebElement element = driver.findElement(By.name("q"));
        // Enter something to search for
        element.sendKeys("Cheese!");
        // Now submit the form. WebDriver will find the form for us from the element
        element.submit();
    }

    @Then("^the page title starts with cheese$")
    public void checkTitle() {
        // Google's search is rendered dynamically with JavaScript.
        // Wait for the page to load, timeout after 10 seconds
        (new WebDriverWait(driver, 10)).until(new ExpectedCondition<Boolean>() {
            public Boolean apply(WebDriver d) {
                return d.getTitle().toLowerCase().startsWith("cheese");
            }
        });
        assertThat(driver.getTitle(), startsWith("cheese"));
        // Should see: "cheese! - Google Search"
    }

    @After()
    public void teardown() {
        driver.quit();
    }
}
{% endhighlight %}
</div>
</div>

## Other tools and frameworks
Other browser testing tools which work with the various language flavours of Cucumber include:
* [Capybara](https://github.com/jnicklas/capybara) (Ruby Acceptance test framework for web applications)
* [Zombie.js](http://zombie.labnotes.org/) (Javascript headless browser)
* [SpookyJS](https://github.com/WaterfallEngineering/SpookyJS) (Javascript headless browser using CasperJS)


## Tips and Tricks
### Re-using the browser window
Closing and re-opening the browser window between your tests will slow them down. To re-use them you can use the [SharedDriver](https://github.com/cucumber/cucumber-jvm/blob/master/examples/java-webbit-websockets-selenium/src/test/java/cucumber/examples/java/websockets/SharedDriver.java) wrapper rather than calling Webdriver directly.
### Embedding Screenshots
See the [example code for embedding screenshots](reports.html#embedding_screenshots).

## Example Projects
* [java-webbit-websockets-selenium](https://github.com/cucumber/cucumber-jvm/tree/master/examples/java-webbit-websockets-selenium)
* [Guardian Frontend integration tests](https://github.com/guardian/frontend/tree/master/integration-tests)

