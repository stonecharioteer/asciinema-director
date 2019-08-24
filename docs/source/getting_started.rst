Getting Started
====================

I've used asciinema for a very long time and the biggest problem is making
flawless recordings. It is hard to avoid making mistakes, especially when
creating a long recording. Also, sometimes, you're in the middle of recording
and you want to consult documentation.

`asciinema-director` is a library that uses `pexpect` to interact with `asciinema`
to create the `cast` files for you. It makes it so that you can write your
commands into a `screenplay` file, sit back and relax.


Installation
--------------

Use pip.

.. code:: bash

    $ pip install asciinema-director
    $ asciinema-director --help                                                                                                                                                      git:(master*)
    Usage: asciinema-director [OPTIONS] SRC DEST

    Options:
    -D, --delay FLOAT
    --help             Show this message and exit.


Screenplay File
-----------------

The screenplay file is the instruction file that you provide.

.. todo::

    Design the screenplay file format.
