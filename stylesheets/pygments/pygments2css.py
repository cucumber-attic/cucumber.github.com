# http://pygments.org/docs/quickstart/
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from TomorrowNightEightiesStyle import TomorrowNightEightiesStyle
print HtmlFormatter(style=TomorrowNightEightiesStyle).get_style_defs('.highlight')