---
layout: bootstrap
title: API
---
# {{page.title}}

This page explains the high level Cucumber API. For more detailed platform-specific API docs see the [Install](/install.html) page.

## Glue code

Between `.feature` files written in [Gherkin](/gherkin.html) and your application there is _glue code_. Glue code can be written in any of the many programming languages supported by Cucumber --- typically in the same language as your application.

![Glue](/images/glue.png)

There are two kinds of glue code --- [Step Definitions](/step-definitions.html) and [Hooks](/hooks.html).