require 'rake/clean'
require 'less'
require 'jsmin'

file 'submodules/gherkin-syntax-highlighters' do
  mkdir_p 'submodules/gherkin-syntax-highlighters'
  Dir.chdir 'submodules' do
    sh `git clone git://github.com/cucumber/gherkin-syntax-highlighters.git`
  end
end

shjs = (
  Dir['submodules/gherkin-syntax-highlighters/shjs/shjs-0.6-src/sh_main.min.js'] +
  Dir['submodules/gherkin-syntax-highlighters/shjs/shjs-0.6-src/lang/sh_{cpp,csharp,java,javascript,properties,python,ruby,scala,sh,xml}.min.js'] +
  Dir['submodules/gherkin-syntax-highlighters/shjs/sh_{clojure,lua}.js'] +
  Dir['submodules/gherkin-syntax-highlighters/shjs/sh_gherkin_{en}.js']
)

task :list_shjs do
  puts shjs.to_a.flatten.map{|js| File.basename(js).match(/([^\.]+).*/)[1] }
end

CLEAN.include('javascripts/shjs.js')
file 'javascripts/shjs.js' => shjs do
  File.open('javascripts/shjs.js', 'w') do |io|
    shjs.each do |js|
      io.write(';')
      io.write(JSMin.minify(IO.read(js)))
    end
  end
end
task :shjs_gherkin => 'javascripts/shjs.js'

file 'stylesheets/shjs.css' => Dir['submodules/gherkin-syntax-highlighters/shjs/css/*.less'] do
  css = Dir.chdir('submodules/gherkin-syntax-highlighters/shjs/css') do
    Less::Parser.new.parse(IO.read('sh_tomorrow_night_eighties.less')).to_css
  end
  File.open('stylesheets/shjs.css', 'wb') {|out| out.write(css)}
end

task :default => [:shjs_gherkin, 'stylesheets/shjs.css']
