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
    cd `$HOME/.python/profile_default/startup`:
    wget https://raw.github.com/rocky/ipython-trepan/master/trepanmagic.py
```
