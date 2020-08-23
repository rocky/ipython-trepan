ipython-trepan
===================

IPython extension for using the [python trepan](https://pypi.python.org/pypi?:action=display&name=trepan) debugger.

## Installation

To install execute the the following code snippet in an IPython shell or IPython notebook cell:

```
    %install_ext https://raw.github.com/rocky/ipython-trepan/master/trepanmagic.py
    %load_ext trepanmagic
```

or put *trepanmagic.py* in `$HOME/.python/profile_default/startup`:

```
    cd $HOME/.ipython/profile_default/startup
    wget https://raw.github.com/rocky/ipython-trepan/master/trepanmagic.py
```

## Usage

IPython magic functions that are added:

 * `%trepan_eval` &ndash; evaluate a Python statement under the debugger
 * `%trepan` &ndash; run the debugger on a Python program
 * `%trepan_pm` &ndash; do post-mortem debugging

### Example

```
$ ipython
Python 2.7.8 (default, Apr  6 2015, 16:25:30)
...

In [1]: %load_ext trepanmagic
trepanmagic.py loaded
In [2]: import os.path
In [3]: %trepan_eval os.path.join('foo', 'bar')
(/tmp/eval_stringS9ST2e.py:1 remapped <string>): <module>
-> 1 (os.path.join('foo', 'bar'))
(trepan2) s
(/home/rocky/.pyenv/versions/2.7.8/lib/python2.7/posixpath.py:68): join
-> 68 def join(a, *p):
(trepan2) s
(/home/rocky/.pyenv/versions/2.7.8/lib/python2.7/posixpath.py:73): join
-- 73     path = a
(trepan2) c
Out[3]: 'foo/bar'
In [4]:
```

See also the [examples](https://github.com/rocky/ipython-trepan/tree/master/examples) directory.
