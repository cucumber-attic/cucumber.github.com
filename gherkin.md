---
layout: bootstrap
title: Gherkin
---
# {{page.title}}

Gherkin is the format for Cucumber Specifications. Technically speaking it is a [small computer language](http://www.martinfowler.com/bliki/BusinessReadableDSL.html) with a well-defined syntax, but
it's so simple that you don't have to know how to program in order to use it.

Gherkin has following Characteristics:
- Gherkin is a Domain Specific language which is used for behavior specifications.
- Gherkin is a line-oriented language that uses indentation to define structure.
- Most lines in Gherkin start with a Keyword.
- Line endings terminate statements.

Here is a simple Gherkin document:

{% highlight gherkin %}
Feature: Password management
  In order to manage passwords
  As a registered user
  I want to specify password management rules
  
  Scenario: Forgot password
    Given a user with email "cukes@cukes.info" exists
    When I ask for a password reset
    Then an email with a password reset link should be sent
{% endhighlight %}

The only syntax here is the colored keywords (Feature, Scenario, Given etc) at the beginning of each line. The rest is entirely up to you.

Gherkin documents are stored in regular text files with a `.feature` file extension. The file above could
be stored in a `password_management.feature` file.

When Cucumber runs a feature file, it divides a feature file into feature, scenario and steps. lets discuss each one in more detail:

- Feature:
      - When cucumber scans a .feature file, it looks for a keyword Feature.So every feature file should contain only one Feature Keyword.
      - Line that follows after Feature Keyword is the Title of the Feature.
      - Title of the Feature is used in Test Results.
      - Three Indented lines after the Feature Keyword line start a feature.
      - These three lines specify the INTENT of the feature file.
      - Example of these three lines:
          In order to achieve something
          As a Registered User
          I want to implement xyz functionality
      - Untill cucumber encounters another keyword like Scenario or Scenario Outline etc, all text will be considered in keyword Features' scope.
      - A Feature contains multiple Scenarios. 

- Scenario:
      - Each Feature file may have multiple scenarios.
      - Each Scenario start with a Keyword Scenario.
      - Line that follwos Keyword Scenario is Scenario Title.
      - Scenario Title is used in Test Reports but is optional.
      - Each Scenario can be considered as a Test Case.
      - Scenario can contain multiple Steps.

- Steps:
      - Each Scenario contain Steps.
      - Step can be considered as Test Steps.
      - Steps are as following: Given, When, Then, And, But

- Given:
      - Similar to Pre Conditions of the use cases.
      - Given Steps put the system in known state which is necessary for the user action( followed in next step) 
      - Avoid talking about user interaction in Given Steps.
      - Example: Given User is on login Page

- When:
      - The purpose of When steps is to describe the user action.
      - Example: When user clicks Login Button

- Then:
      - The purpose of Then steps is to observe expected outcomes. 
      - The observations should be related to the business value/benefit in your feature description.
      - Example: Then user is on Home Page


TODO: MORE
