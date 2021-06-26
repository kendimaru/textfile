
Functions that enables us to write out or read from with text file in shorter syntax
than using only standard library.

Install
-------

::

    pip install textfile


Usage
-----

Create file and write text to it::

    >>> import textfile
    >>> textfile.write("a.txt", "any string value")

Read text from file::

    >>> import textfile
    >>> textfile.read("a.txt")
    "any string value"

The benefit to use textfile
---------------------------

By using ``textfile``, it is possible to shorten your program on a specific situation.

If you often write code like::

    with open("somefile.txt") as f:
        f.write("any string value")

You can rewrite those codes to::

    textfile.write("somefile.txt", "any string value")

And other functions in ``textfile`` library are made of the same consept.

What situation does textfile fits?
----------------------------------

API that is simple to use, is less flexibility.
It means that, it is not recommended to use in such a programs that is required speed or strictness.

But I think that it will not be a matter in almost all situations of our programming.

I courage you to use ``textfile`` as much as possible you can.
If you do so, increase the readability of your code and suppress the bug.

Is this document written in strange English?
--------------------------------------------
Kenjimaru, the author of this document, I am Japanese and am not familiar to English.

So, if you read this document, and find anything to fix, feel free to contact me,
and I will appreciate.

