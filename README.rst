
Wrapper functions of codes of text file operation that are very commonly seen.
By using ``textfile``, readability of our program will be improve!

Install
-------

.. code-block:: Shell

    > pip install textfile


Very basic usage
----------------

Create file and write text to it.

.. code-block:: python

    >>> import textfile
    >>> textfile.write("a.txt", "any string value")

Read text from text file.

.. code-block:: python

    >>> import textfile
    >>> textfile.read("a.txt")
    "any string value"

Use cases
---------

Write string to text file:

.. code-block:: python

    textfile.write("somefile.txt", "any string value")

Read entire string from text file:

.. code-block::

    textfile.read("somefile.txt")

Replace string in text file:

.. code-block::

    textfile.replace("somefile.txt", "replaced", "replacement")

Append string to text file:

.. code-block::

    textfile.append("somefile.txt", "text to append")

Insert string to text file:

.. code-block::

    textfile.insert("somefile.txt", "text to insert", line=10)


Just a implementation of facade pattern
---------------------------------------

``textfile`` wraps python algorithms that are very commonly used
in the purpose of to more simplify basic operations.

This is just a facade pattern.

The side effect of simplify the interface of text file operation, gets less flexibility.
Further more, it becomes hard to do speed tuning.

But I think that those are not a matter in almost all situations of our programming.

We should pay more attention to code readability!

I courage you to use ``textfile`` as much as possible you can.
If you do so, the readability of your code will increase, and will suppress many bugs.


Is this document written in strange English?
--------------------------------------------
Kenjimaru, the author of this document, I am Japanese and am not familiar to English.

If you read this document, and find anything should be fixed, feel free to contact me,
and I will appreciate.

