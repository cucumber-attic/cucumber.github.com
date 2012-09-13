This is the source of the new http://cukes.info site

To run:

```
jekyll --safe --server --auto
```

## Syntax highlighting

To syntax highlight this code:

```
def foo
end
``` 

Use this markup:

```
<pre class="sh_ruby"><code>{% capture code %}def foo
end
{% endcapture %}{{ code | xml_escape }}</code></pre>
```

That will render it something like this:

```ruby
def foo
end
```

Except that the syntax highlighting engine is SHJS, not Pygments. The main reason is that we have more control over SHJS than Pygments syntax highlighting.

To see all available labguages, run `rake list_shjs`