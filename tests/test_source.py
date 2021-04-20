import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source Class.
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test.
        '''

        self.new_source = Source("abc-news", "ABC News", "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.", "https://abcnews.go.com", "general", "en", "us")

    def test_instance(self):
        '''
        Test case to test if object instance is created.
        '''

        self.assertTrue(isinstance(self.new_source, Source))