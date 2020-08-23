ipython-trepan
===================

IPython extension for using the [python trepan](https://pypi.python.org/pypi?:action=display&name=trepan) debugger.

## Installation

Normal installation is via pip:

```
pip install git+https://github.com/rocky/ipython-trepan
```

If you'd like the extension to be loaded automatically you can put the extension file directly under your
 `$HOME/.ipython/profile_default/startup`, by doing:


```
    cd $HOME/.ipython/profile_default/startup
    wget https://raw.github.com/rocky/ipython-trepan/master/trepanmagic.py
```
Now `ipython` will load it automatically every time it starts.

## Usage

First load the extension in an IPython shell or IPython notebook cell:

```
    %load_ext trepanmagic
```

This adds the following IPython magic functions:

 * `%trepan_eval` &ndash; evaluate a Python statement under the debugger
 * `%trepan` &ndash; run the debugger on a Python program
 * `%trepan_pm` &ndash; do post-mortem debugging

### Example

```
ipython
Python 3.7.5 (default, Oct 25 2019, 15:51:11)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.13.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: %load_ext trepanmagic

trepanmagic.py loaded

In [2]:  import os.path

In [3]: %trepan_eval os.path.join('foo', 'bar')
(<string>:1 remapped <string>): <module>
(trepan3k) s
(/home/stas/anaconda3/envs/main/lib/python3.7/posixpath.py:75): join
-> 75 def join(a, *p):
a = 'foo'
p = ('bar',)
(trepan3k) s
(/home/stas/anaconda3/envs/main/lib/python3.7/posixpath.py:80): join
-- 80     a = os.fspath(a)
(trepan3k) c
Out[3]: 'foo/bar'
```

See also the [examples](https://github.com/rocky/ipython-trepan/tree/master/examples) directory.
