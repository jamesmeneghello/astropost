Astropost
=========

Simple API for posting comments to various Australian news websites.

This project was developed primarily due to the increased amount of astroturfing apparent on Australian news websites
(particularly News Ltd.). If you're going to spam the shit out of a comments section and ruin the entire point of
having the ability to comment, why not do it with a nice API?


Simple Usage
------------

Usage should be simple. Create a post and specify desired fields - any omitted (but required) fields will be randomised.

    >>> p = astropost.Post(name="poster name", email="email@example.com", body="a comment that nobody will read")
    >>> p.body
    'a comment that nobody will read'
    >>> p.location
    'Somerandomcityname'

Because unfilled fields (aside from comment/body) will be randomised, minimum usage is:

    >>> p = astropost.Post("Some interesting comment that will surely add to the discussion and won't just say ELECTION NOW!!!")

Once a post has been created, we create the desired interface, direct it to the appropriate page and send the post.

    >>> astropost.Engine().post('http://www.heraldsun.com.au/news/national/...', p)
    true

We can also enable debug mode (to test values, but not actually send the data) by enabling it during the call:

    >>> astropost.Engine().set_debug(True).post('http://www.heraldsun.com.au/news/national/...', p)


Supported Interfaces
--------------------

Library currently supports the following:

- most Australian News Ltd. sites (news.com.au, hun, perthnow, etc).

Awaiting support on:

- ABC Unleashed articles (since these seem to be the only ones with comments)

Further down the track:

- SMH (requires an account through recaptcha activation or facebook/twitter/linkedin)