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
This is only mildly complicated due to the need to specify a classpath etc.

In short, use the following script:
{% highlight bash %}
CLASSPATH=lib/*
CLASSPATH=$CLASSPATH:classes
CLASSPATH=$CLASSPATH:test-classes

java \
    -classpath $CLASSPATH \
    cucumber.api.cli.Main \
    --glue foldername \ # the foldername containing compiled glue code
    path/to/feature/folder
{% endhighlight %}

In this example, the directory structure looks like so (slightly modified from the Cucumber-JVM "Hello World" example):

```
lib/
    cucumber-core.jar
    cucumber-java.jar
    cucumber-jvm-deps.jar
    gherkin.jar
src/
    main/java/skeleton/Belly.java
    test/
         java/skeleton/Stepdefs.java
         resources/cucumber.properties
         resources/skeleton/belly.feature
```

The sources are compiled into two folders: target/classes for the actual code, and target/test-classes for step definitions known as "glue code".
This then explains the classpath settings in the script above:

1. The lib folder containing the Cucumber jars.
2. The compiled source code.
3. The compiled glue code.

...and also the argument to '--glue'.

Running the above script should (if everything works correctly) run your features.

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
Apart from the usual classpath/compile/clean targets, to actually run Cucumber-JVM you will need the following xml.
Note that the 'compile-test' target compiles the test classes which include the glue code for steps etc.
It uses the same directory structure as the Command-line example above.

{% highlight xml %}
    <target name="runcukes" depends="compile-test">
        <java classname="cucumber.api.cli.Main" fork="true" 
            failonerror="false" resultproperty="cucumber.exitstatus">
            <classpath refid="classpath"/>
            <arg value="--glue"/>
            <arg value="skeleton"/>
            <arg value="src/test/resources"/>
        </java>

        <fail message="Cucumber failed">
            <condition>
                <not>
                    <equals arg1="${cucumber.exitstatus}" arg2="0"/>
                </not>
            </condition>
        </fail>
    </target>
{% endhighlight %}

Simply run `ant runcukes` to run the tests.

### Gradle
TODO

## Options

TODO: Explain all the options
