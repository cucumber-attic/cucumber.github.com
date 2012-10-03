# -*- coding: utf-8 -*-
"""
tomorrow night bright
---------------------

Port of the tomorrow night bright color scheme for Vim.
"""

from pygments.style import Style
from pygments.token import Comment, Error, Keyword, Name, Number, Operator, \
                           Punctuation, String, Text, Generic

BACKGROUND   = "#2d2d2d"
CURRENT_LINE = "#393939"
SELECTION    = "#515151"
FOREGROUND   = "#cccccc"
COMMENT      = "#999999"
RED          = "#f2777a"
ORANGE       = "#f99157"
YELLOW       = "#ffcc66"
GREEN        = "#99cc99"
AQUA         = "#66cccc"
BLUE         = "#6699cc"
PURPLE       = "#cc99cc"


class TomorrowNightEightiesStyle(Style):

    """
    Port of the tomorrow night bright color scheme.
    """

    default_style = ''

    background_color = BACKGROUND
    highlight_color = SELECTION

    styles = {
        
        Comment:                COMMENT,
        Text:                   FOREGROUND,

        Keyword:                PURPLE,
        Keyword.Type:           YELLOW,
        Operator.Word:          '',

        String:                 GREEN,
        String.Char:            FOREGROUND,

        Name.Builtin:           RED,
        Name.Variable:          '',
        Name.Variable.Instance: RED,
        Name.Constant:          GREEN,
        Name.Class:             YELLOW,
        Name.Function:          BLUE,
        Name.Namespace:         YELLOW,
        Name.Exception:         RED,
        Name.Tag:               BLUE,
        #Name.Attribute:        '',
        Name.Decorator:         AQUA,

        Generic.Deleted:        RED,
        Generic.Inserted:       GREEN,
        Generic.Heading:        "bold " + FOREGROUND,
        Generic.Subheading:     "bold " + AQUA,
        Generic.Prompt:         "bold " + COMMENT

}