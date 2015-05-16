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

## Usage

IPython magic functions that are added:

 * `%trepan_eval` &ndash; evaluate a Python statement under the debugger
 * `%trepan` &ndash; run the debugger on a Python program
 * `%trepan_pm` &ndash; do post-mortem debugging

See the [examples](https://github.com/rocky/ipython-trepan/tree/master/examples) directory for examples of how these work.
