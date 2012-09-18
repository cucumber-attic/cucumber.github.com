# How to create a new CSS files

Download a `.vim` theme from https://code.google.com/p/vimcolorschemetest/

Now, generate a .py and a .css file:

```
python vim2pygments.py native.vim > native.py
python pygments2css.py > native.css
```

Just change the name from 'native' to whatever else