---
layout: bootstrap
title: Good practices
---
# {{page.title}}

Cucumber can be used differently in different contexts. You don't have to follow the following recommendations but it was noticed that they work better across different situations:

### Gherkin layer
* Use declarative style as:
  * look of app can be changed without updating features
  * scenarios written in domain language are read better
  * scenarios are read easier if they are short
  * makes your scenarios [WET](http://programmers.stackexchange.com/questions/131180/what-is-the-meaning-of-wet-code)

  At the opposite imperative style:
  * Increases the cost of change

For more details read [Ben Mabey's article](http://benmabey.com/2008/05/19/imperative-vs-declarative-scenarios-in-user-stories.html)

* If your feature contains more than 20 scenarios, consider dividing them to separate features. It will 
* Language across scenarios should be consistent. Prefer domain-specific language to UI-specific language
* All scenarios need to be independent from each other. It allows running them in parallel and gives possibility to debug/review them without immersing into other scenarios. No expectations about state should be assumed. All dependencies that aren’t related to the goal of scenario should be moved to automation layer. The automation layer should prepopulate data with sensible defaults and setup dependencies.
* Include the domain experts and customers into writing scenarios. Don’t get one person to write them. It’s not about one person’s view
* Scenarios should explain how feature works at a high level. Implementation details shouldn’t be included into scenarios. Avoid tying scenarios to the UI by referencing page elements, controls.
* Avoid the temptation to explore every combinatorial possibility. Only important cases should be illustrated. Other cases are better to be situated at lower levels (unit, integration)
* When writing Then, ask questions “Is there anyting else that would happen?”
* If you need additional tests, put them into separate file (main file should exist for communication and sharing understanding)

### Concrete examples vs Classes of equivalence##

Pluses of concrete examples:
* Illustrate how feature works
* Stakeholders may provide missed edge cases if they see existing one

Pluses of classes of equivalence:
* Decrease cost of change if concrete value changes
