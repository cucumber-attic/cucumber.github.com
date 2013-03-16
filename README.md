This is the source of the new http://cukes.info site

## Viewing locally

You need ruby 1.9.3, 2.0.0 or newer.

```
gem install bundler
bundle
foreman start
open http://localhost:4000
```

Whenever you change a `*.md` file the site should be automatically rebuilt.

## Contributing

There should be `*.md` files lying around that don't have a lot of content in them. Feel free to add content here.
You can do this straight in your browser via https://github.com/cucumber/cucumber.github.com. Find the file and click Edit button. 

You can also add new `.md` pages, but if you do, please update the navigation menu as well---you'll find it in `_config.yml`.

Keep in mind that this site aims to document everything Cucumber in a platform neutral way, so if you're adding code snippets, please use a tab pane (see `step-definitions.md`) so that users can see code examples in various programming languages. You don't have to add code for all languages, we'll do our best to fill that in afterwards.
