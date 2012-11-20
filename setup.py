try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Commenting API for Australian news sites',
    'author': 'James Meneghello',
    'url': 'http://github.com/murodese/astropost',
    'download_url': 'https://github.com/Murodese/astropost/archive/master.zip',
    'author_email': 'murodese@gmail.com',
    'version': '0.1',
    'install_requires': ['mechanize', 'faker'],
    'packages': ['astropost'],
    'scripts': [],
    'name': 'astropost'
}

setup(**config)