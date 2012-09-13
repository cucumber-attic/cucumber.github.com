---
layout: default
title: Cucumber-JVM Installation
---
## {{page.title}}

Cucumber-JVM consists of several modules (jars). You will always need the `cucumber-core` module, which contains the main logic for parsing and executing your Gherkin feature files.

### Programming Language modules

In addition to `cucumber-core` you will also need a programming language-specific module, depending on what programming language you are using. The available programming language modules are:

| Language/Platform              | Jar file            |
| ------------------------------ | ------------------- |
| Java                           | `cucumber-java`     |
| Clojure                        | `cucumber-clojure`  |
| Groovy                         | `cucumber-groovy`   |
| Ioke                           | `cucumber-ioke`     |
| JavaScript (Rhino interpreter) | `cucumber-rhino`    |
| Python (Jython interpreter)    | `cucumber-jython`   |
| Ruby (JRuby interpreter)       | `cucumber-jruby`    |
| Scala                          | `cucumber-scala`    |

### Dependency Injection modules for cucumber-java

If your programming language is Java you will be writing glue code ([Step Definitions](step-definitions.html) and [Hooks](hooks.html)) in plain old Java classes. Cucumber will create a new instance of each of your glue code classes before each [Scenario](gherkin.html#scenario). If all of your glue code classes have an empty constructor you don't need anything else. However, most projects will benefit from a [Dependency Injection](dependency-injection) module to organize your code better.

The available Dependency Injection modules are:

| Dependency Injection Container | Jar file                 |
| ------------------------------ | ------------------------ |
| PicoContainer                  | `cucumber-picocontainer` |
| Guice                          | `cucumber-guice`         |
| OpenEJB                        | `cucumber-openejb`       |
| Spring                         | `cucumber-spring`        |
| Weld                           | `cucumber-weld`          |

### Runners

There are two ways to run Gherkin Features with Cucumber-JVM:

| Runner                         | Jar file                 |
| ------------------------------ | ------------------------ |
| Command Line Interface         | `cucumber-core`          |
| JUnit Runner                   | `cucumber-junit`         |

The JUnit Runner lets you run Cucumber from any tool that understands JUnit. This includes IDEs (such ash IntelliJ or Eclipse) and build tools (such as Ant, Maven or Gradle).

Any build tool can execute command line programs (Cucumber's Command Line Interface), so if you prefer this way to run your features you don't need the `cucumber-junit` module.

This should help you pick the 2 or 3 modules you need. Let's install them:

### Manual download

You can browse your way to the modules you need in the [Sonatype](https://oss.sonatype.org/content/repositories/releases/info/cukes/) repository. Or you can search for them in [Maven Central](https://search.maven.org/).

### Maven

Installing the various `cucumber-*` modules in a Maven project is just a matter of adding them to your `pom.xml` file. Here is the minimal recommended setup:

<pre class="sh_xml"><code>{% capture code %}<dependencies>
    <dependency>
        <groupId>info.cukes</groupId>
        <artifactId>cucumber-picocontaine</artifactId>
        <version>1.0.14</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>info.cukes</groupId>
        <artifactId>cucumber-junit</artifactId>
        <version>1.0.14</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>junit</groupId>
        <artifactId>junit</artifactId>
        <version>4.10</version>
        <scope>test</scope>
    </dependency>
</dependencies>
{% endcapture %}{{ code | xml_escape }}</code></pre>

You don't have to explicitly add a dependency on `cucumber-core` as all the other packages depend on it.

### Ant without Ivy

You'd better take a look at the [java-helloworld build.xml file](https://github.com/cucumber/cucumber-jvm/blob/master/examples/java-helloworld/build.xml)
