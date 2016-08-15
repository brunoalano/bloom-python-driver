bloom-python-driver
=========

Pybloom provides a Python client library to interface with
bloomd servers. The library supports multiple bloomd servers,
and automatically handles filter discovery and sharding.

Features
--------


* Provides a simple API for using bloomd
* Allows for using multiple bloomd servers
   - Auto-discovers filter locations
   - Balance the creation of new filters
   - Explicitly name the location to make filters
* Command pipelining to reduce latency


Install
-------

Download and install from source:

    python setup.py install

Example
------

Using pybloom is very simple, and is similar to using native sets::

    from pybloomd.pybloomd import BloomdClient

    # Create a client to a local bloomd server, default port
    client = BloomdClient(["localhost"])

    # Get or create the foobar filter
    foobar = client.create_filter("foobar")

    # Set a property and check it exists
    foobar.add("Test Key!")
    assert "Test Key!" in foobar

To support multiple servers, just add multiple servers::

    from pybloomd.pybloomd import BloomdClient

    # Create a client to a multiple bloomd servers, default ports
    client = BloomdClient(["bloomd1", "bloomd2"])

    # Create 4 filters, should be on different machines
    for x in xrange(4):
        client.create_filter("test%d" % x)

    # Show which servers the filters are on by
    # specifying the inc_server flag
    print client.list_filters(inc_server=True)

    # Use the filters
    client["test0"].add("Hi there!")
    client["test1"].add("ZING!")
    client["test2"].add("Chuck Testa!")
    client["test3"].add("Not cool, bro.")


Using pipelining is straightforward as well::

    from pybloomd.pybloomd import BloomdClient

    # Create a client to a local bloomd server, default port
    client = BloomdClient(["localhost"])

    # Get or create the foobar filter
    pipe = client.create_filter("pipe").pipeline()

    # Chain multiple add commands
    results = pipe.add("foo").add("bar").add("baz").execute()
    assert results[0]
    assert results[1]
    assert results[2]


