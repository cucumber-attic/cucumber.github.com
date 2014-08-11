---
layout: bootstrap
title: Running Cucumber
---
# {{page.title}}

There are quite a few ways you can run Cucumber. It depends on what programming language you are using and also what build tool
you are using (if any).

* Command Line
* Rake
* Maven
* Ant
* JUnit
* IDEs (Eclipse, IDEA)
 
## Running Cucumber-JVM
### Command Line
TODO

### JUnit
Create one empty class with the `@RunWith(Cucumber.class)` annotation. 
Executing this class as any JUnit test class will run all features found on the classpath in the same package as this class.
The options to be used are defined with the `@CucumberOptions` (`@Cucumber.Options` is deprecated from version 1.1.5).
{% highlight java %}
package somepackage;

import cucumber.api.CucumberOptions;
import cucumber.api.junit.Cucumber;
import org.junit.runner.RunWith;

@RunWith(Cucumber.class)
@CucumberOptions(format = "pretty")
public class RunCukesTest {
}
{% endhighlight %}
### TestNG
TODO

### Android
TODO

#### Android options
TODO

### Maven
TODO

### Ant
TODO

### Gradle
TODO

## Options

TODO: Explain all the options
