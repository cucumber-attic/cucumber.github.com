---
layout: bootstrap
title: Hooks
---
# {{page.title}}

TODO: Write me

There are several types of hooks, but first lets talk about the most basic.

There are @before and @after hooks.

These are called by JUnit before and after each test. 

Java Example:

@Before(order = 1)
public void beforeTest(){
  //Do something before test - like start selenium browser.
}

@After(order = 1)
public void afterTest(Scenario currentScenario){
  //Do something after test - like quit selenium browser.
}

You can set the "order" of @Before hooks and @After hooks. Lowest number first for @Before hooks and highest number first for @After hooks. If the order is the same, they will be run in sequential order. These functions can exist anywhere in your code. 

If you want to make @Before and @After hooks for specific tags, simply use the "value" attribute in the hooks.

Java Example:

@Befter(order = 1, value="cucumber")
public void beforeCucumber(){
  //Slice delicious cucumber
}

@After(order = 1, value = "cucumber")
public void afterCucumber(){
  //eat delicious cucumber
}

You can pass in a Scenario object in any hook by just adding them to the parameters. Scenario objects can be used for supplementing the default cucumber reports. See the "embedding text and screen shots" section at http://cukes.info/reports.html for more details

See http://cukes.info/api/cucumber/jvm/javadoc/cucumber/api/java/Before.html for more options on what can be used with @Before and @After hooks.

See https://github.com/cucumber/cucumber/wiki/Hooks for Ruby hooks.

