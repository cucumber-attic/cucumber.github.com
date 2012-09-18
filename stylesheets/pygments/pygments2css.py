# http://pygments.org/docs/quickstart/
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from native import NativeStyle
print HtmlFormatter(style=NativeStyle).get_style_defs('.highlight')