# -*- coding: utf-8 -*-
"""
    Native Colorscheme
    ~~~~~~~~~~~~~~~~~~

    Converted by Vim Colorscheme Converter
"""
from pygments.style import Style
from pygments.token import Token, Comment, Name, Keyword, Generic, Number, Operator, String

class NativeStyle(Style):

    background_color = '#222222'
    styles = {
        Token:              '#f2f2f2 bg:#222222',
        Generic.Output:     '#444444 bg:#111111',
        Keyword:            '#6ab825 bold',
        Generic.Deleted:    '#0000c0 bg:#008080 bold',
        Number:             '#3677a9',
        Name.Tag:           '#6ab825 bold',
        String:             '#ed9d13',
        Comment:            '#999999 italic',
        Name.Attribute:     '#447fcf',
        Generic.Inserted:   'bg:#0000c0',
        Name.Function:      '#447fcf',
        Generic.Heading:    '#ffffff bold',
        Keyword.Type:       '#bbbbbb bold',
        Generic.Subheading: '#ffffff bold',
        Name.Constant:      '#ed9d13',
        Comment.Preproc:    '#cd2828 bold',
    }
