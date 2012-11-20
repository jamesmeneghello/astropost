"""Simple API for posting comments to various Australian news websites"""
VERSION = (0, 0, 1)
__version__ = '.'.join(map(str, VERSION))
__author__ = 'James Meneghello'
__contact__ = 'murodese@gmail.com'
__homepage__ = 'https://github.com/murodese/astropost'
__all__ = ('Post', 'Engine')

import faker
import re
import inspect
import interfaces
import logging

class Post(object):
    def __init__(self, body, name=None, email=None, location=None):
        """
                Creates a post containing body that can be passed to an astropost engine for submission to any
                supported news site. Only body is required - any other omitted field will have data auto-generated to
                suit.

                :param body: Text to be submitted as the comment.
                :param name: (optional) Author of comment.
                :param email: (optional) Email address of author.
                :param location: (optional) Location of author.
                """

        self.body = body

        if name:
            self.name = name
        else:
            self.name = faker.Faker().name()

        if email:
            self.email = email
        else:
            self.email = faker.Faker().email()

        if location:
            self.location = location
        else:
            self.location = faker.Faker().city()


class Engine(object):
    debug = False

    def __init__(self):
        pass

    def set_debug(self, debug):
        """
        Sets the engine to debug mode - will test pages, but won't submit data
        :param debug: True/False
        :return: Engine
        """
        self.debug = debug
        return self

    def post(self, url, post):
        """
        Automatically retrieves a suitable interface and posts comment

        :param url: URL of the article to post comment to
        :param post: Post object containing comment details
        """
        logging.info('[Engine] Sending post to interface for processing..')
        self._get_interface(url).post(url, post, self.debug)

    def vote(self, url, poll):
        """
        Automatically retrieves an interface and casts a vote for a poll

        :param url: URL containing poll to be voted upon
        :param poll: Poll object containing poll details (and desired selection)
        """
        logging.info('[Engine] Sending vote to poll..')
        # TODO: Implement poll voting

    def _get_interface(self, url):
        """
        Retrieves an Astropost interface based on the URL that the post is targetted at.

        :param url: URL to the news article (that has commenting facility)
        :return: Instance of the interface suitable for use
        """
        logging.info('[Engine] Getting interface for url: ' + url)

        interface_module = interfaces
        for name, obj in inspect.getmembers(interface_module):
            if inspect.isclass(obj):
                if issubclass(obj, interface_module.Interface) and obj is not interface_module.Interface:
                    for line in obj.urls:
                        if re.match(line, url) is not None:
                            logging.info('[Engine] Found a suitable interface: ' + obj.__name__)
                            return obj()

        logging.error('[Engine] No suitable interface found!')
        return None