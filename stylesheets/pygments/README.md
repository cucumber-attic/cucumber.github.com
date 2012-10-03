# How to create a new CSS files

Download a `.vim` theme from https://code.google.com/p/vimcolorschemetest/

Now, generate a .py and a .css file:

```
python vim2pygments.py native.vim > native.py
python pygments2css.py > native.css
```

Just change the name from 'native' to whatever else. You also have to change this in `pygments2css.py`

After generation, you may have to change the generated css on line 2 from:

```
.highlight { ... }
```

to

```
.highlight pre { ... }
```

This is to make the CSS play nice with Bootstrap CSS.