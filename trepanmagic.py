# -*- coding: utf-8 -*-
"""
===========
trepantmagic
===========

IPython Magics for trepan debugging.

.. note::

  The ``trepan`` module needs to be installed first

.. sourcecode:: ipython

In [1]: %load_ext trepanmagic

In [2]: import os

In [3]: %trepan_eval os.path.join("a", "b")

In [4]: %trepan --highlight -- pygmentize -f terminal /tmp/example.py 1 3

Usage
=====

The following magic commands are provided:

``%trepan_eval``

Use ``%trepan_eval`` to evaluate an expression under the trepan debugger

Evaluates an expression under the trepan debugger

``%trepan``

Use ``%trepan`` to invoke a top-level Python program with arguments.
You can use ``--`` to separate the debugger arguements from the
program's arguements



    %trepan --highlight -- pygmentize -f terminal /tmp/script.py
"""

import IPython
if IPython.version_info[0] < 3:
    raise ImportError, ("You need IPython 3.x, got %d.%d%d" %
                        IPython.version_info[:3])

from IPython.core.magic import (register_line_magic
                                , line_magic, Magics, magics_class
                                # , cell_magic
                                # , register_cell_magic
                                # , register_line_cell_magic
                                )
import IPython.core.ultratb as ultratb
try:
    import trepan.api
except ImportError:
    raise ImportError, "You need trepan installed: pip install trepan"

import trepan.cli
import shlex
from trepan import exception as Mexcept

@magics_class
class TrepanMagics(Magics):
    """Magics related to trepan debugging"""
    def __init__(self, shell):
        super(TrepanMagics, self).__init__(shell)
        self.shell = shell

    @line_magic
    def trepan_eval(self, python_statement):
        """%trepan_eval *python-expression*"""
        tb_fn = lambda etype, value, tb: \
            self.shell.showtraceback((etype, value, tb), tb_offset=0)

        try:
            return trepan.api.run_eval(python_statement,
                                       start_opts = {'force': True,
                                                     'tb_fn': tb_fn},
                                       debug_opts = {'from_ipython': self.shell},
                                       globals_=self.shell.user_ns)
        except Mexcept.DebuggerQuit:
            pass

    @line_magic
    def trepan(self, line):
        """%trepan *trepan-options [--] *python-script* [*args*...]"""
        sys_argv = shlex.split('trepan --from_ipython ' + line)

        tb_fn = lambda etype, value, tb: \
            self.shell.showtraceback((etype, value, tb), tb_offset=1)

        try:
            return trepan.cli.main(sys_argv=sys_argv)
        except Mexcept.DebuggerQuit:
            pass

def load_ipython_extension(ip):
    # The `ipython` argument is the currently active `InteractiveShell`
    # instance, which can be used in any way. This allows you to register
    # new magics or aliases, for example.
    magicsTrepan = TrepanMagis(ip)
    ip.register_magics(MagicsTrepan)
    print("\ntrepanmagic.py loaded")

magicsTrepan = TrepanMagis(ip)
ip.register_magics(magicsTrepan)
