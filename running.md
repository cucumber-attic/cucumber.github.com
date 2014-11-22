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
cucumber.api.cli.Main --format pretty --format json:directorypath/filename.json --glue packagename /pathtogeneratedtestclasses/

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
### Cucumber command line options
 
    -g, --glue PATH                        Where glue code (step definitions and hooks) is loaded from.
    -f, --format FORMAT[:PATH_OR_URL]      How to format results. Goes to STDOUT unless PATH_OR_URL is specified.
                                           Built-in FORMAT types: junit, html, pretty, progress, json.
                                           FORMAT can also be a fully qualified class name.
    -t, --tags TAG_EXPRESSION              Only run scenarios tagged with tags matching TAG_EXPRESSION.
    -n, --name REGEXP                      Only run scenarios whose names match REGEXP.
    -d, --[no-]-dry-run                    Skip execution of glue code.
    -m, --[no-]-monochrome                 Don't colour terminal output.
    -s, --[no-]-strict                     Treat undefined and pending steps as errors.
        --snippets [underscore|camelcase]  Naming convention for generated snippets. Defaults to underscore.
        --dotcucumber PATH_OR_URL          Where to write out runtime information. PATH_OR_URL can be a file system
                                           path or a URL.
    -v, --version                          Print cucumber version.
    -h, --help                             Shows options that can be used with cucumber cli.
