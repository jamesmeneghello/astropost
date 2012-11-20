import unittest
import astropost
import logging

class TestEngine(unittest.TestCase):
    def test_get_interface(self):
        e = astropost.Engine()
        e.set_debug(True)

        i = e._get_interface(
            'http://www.perthnow.com.au/news/internet-abuse-rife-among-000-cops/story-e6frg12c-1226518800665')
        self.assertIsInstance(i, astropost.interfaces.NewsLimited)
        self.assertNotIsInstance(i, astropost.interfaces.SMH)

        i = e._get_interface(
            'http://www.news.com.au/national/forecasters-take-flak-over-late-alert/story-fndo4ckr-1226518825034')
        self.assertIsInstance(i, astropost.interfaces.NewsLimited)
        self.assertNotIsInstance(i, astropost.interfaces.SMH)

        i = e._get_interface(
            'http://www.heraldsun.com.au/entertainment/much-maligned-bond-girl-is-getting-a-serious-image-upgrade-as-highlighted-in-skyfall/story-e6frf96f-1226518987168')
        self.assertIsInstance(i, astropost.interfaces.NewsLimited)
        self.assertNotIsInstance(i, astropost.interfaces.SMH)

        i = e._get_interface(
            'http://www.abc.net.au/news/2012-11-18/south-east-qld-warned-of-more-storms-to-come/4377954')
        self.assertNotIsInstance(i, astropost.interfaces.NewsLimited)
        self.assertNotIsInstance(i, astropost.interfaces.SMH)
        self.assertIsInstance(i, astropost.interfaces.ABC)

    def test_post(self):
        p = astropost.Post('This is a test!')

        logger = logging.getLogger().setLevel(logging.DEBUG)
        astropost.Engine().set_debug(True).post(
            'http://www.perthnow.com.au/news/internet-abuse-rife-among-000-cops/story-e6frg12c-1226518800665', p)

if __name__ == '__main__':
    unittest.main()