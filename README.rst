Roman numeral converter
=======================

Description
------------

This is a simple Python script which converts arabic numeral into Roman numerals. You need Python 3.7+ and mypy to run it.


Getting Python3 and pip
-----------------------

Please refer to the Python wiki to determine how you should install Python regarding your operating system:
https://wiki.python.org/moin/BeginnersGuide/Download

If your operating system or Linux distribution is not listed, check wiki. For example for Arch Linux go to Arch wiki.

The same applies to pip: https://pip.pypa.io/en/stable/installing/


Getting mypy
------------

Mypy is an optional static checker. It can be obtained through pip.

::

    $ pip install mypy


Running mypy
------------

You can typecheck the script just by typing in the console:

::

    $ mypy roman_numeral_converter.py

|

If you need more information or troubleshooting advice, please refer to the mypy documentation: https://mypy.readthedocs.io/en/stable/


Running
-------

Firstly you need clone GitHub repository using

::

    $ git clone

|

and then go into folder you just cloned. Open console there and simply type:

::

    python roman_numeral_converter.py <your-arabic-number>

|

The results should be printed in the console.

You can receive help by typing:

::

    $ roman_numeral_converter -h


Running tests
-------------

In script folder open console and type:

::

    $ python test_roman_numeral_converter

|

The results will appear in the console.



