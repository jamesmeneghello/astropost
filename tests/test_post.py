import unittest
import astropost

class TestPost(unittest.TestCase):
    def test___init__(self):
        p = astropost.Post('some comment')
        self.assertIsInstance(p, astropost.Post)
        self.assertNotEqual(p.name, '')
        self.assertNotEqual(p.location, '')
        self.assertNotEqual(p.email, '')

        p = astropost.Post(name='James', location='Perth', email='bob@fred.com', body="something")
        self.assertIsInstance(p, astropost.Post)
        self.assertEqual(p.name, 'James')
        self.assertEqual(p.location, 'Perth')
        self.assertEqual(p.email, 'bob@fred.com')
        self.assertEqual(p.body, 'something')


if __name__ == '__main__':
    unittest.main()