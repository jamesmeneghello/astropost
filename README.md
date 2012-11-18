Astropost
=========

Simple API for posting comments to various Australian news websites.

This project was developed primarily due to the increased amount of astroturfing apparent on Australian news websites
(particularly News Ltd.). If you're going to spam the shit out of a comments section and ruin the entire point of
having the ability to comment, why not do it with a nice API?

Simple Usage
------------

Usage should be simple. Create a post and specify desired fields - any omitted (but required) fields will be randomised.

    >>> p = astropost.post.Post(name="poster name", email="email@example.com", body="a comment that nobody will read")
    >>> p.body
    'a comment that nobody will read'
    >>> p.location
    'Somerandomcityname'

Once a post has been created, we create the desired interface, direct it to the appropriate page and send the post.

    >>> eng = astropost.Engine()
    >>> eng.post('http://www.heraldsun.com.au/news/national/forecasters-take-flak-over-late-alert/story-fndo45r1-1226518825034', p)
    true