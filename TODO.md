* Nav hierarchy. Use subfolders.
* http://stackoverflow.com/questions/9053066/sorted-navigation-menu-with-jekyll-and-liquid
* http://stackoverflow.com/questions/6366188/jekyll-select-current-page-url-and-change-its-class

<div class="tab-content">
  <div class="tab-pane active" id="tab1">
    <pre class="sh_ruby"><code>{% capture code %}Given(/I have (\d+) cukes in my belly/) do |cukes|
end{% endcapture %}{{ code | xml_escape }}</code></pre>
  </div>
  <div class="tab-pane" id="tab2">
    <pre class="sh_java"><code>{% capture code %}@Given("I have (\\d+) cukes in my belly")
public void cukesInTheBelly(int cukes) {
}{% endcapture %}{{ code | xml_escape }}</code></pre>
  </div>
  <div class="tab-pane" id="tab3">
    <pre class="sh_groovy"><code>{% capture code %}@Given("I have (\\d+) cukes in my belly")
public void cukesInTheBelly(int cukes) {
}{% endcapture %}{{ code | xml_escape }}</code></pre>
  </div>
  <div class="tab-pane" id="tab3">
    <pre class="sh_fsharp"><code>{% capture code %}let [<Given>] ``I have entered (.*) into the calculator``(number:int) = 
  Calculator.Push(number)
  {% endcapture %}{{ code | xml_escape }}</code></pre>
  </div>
</div>
