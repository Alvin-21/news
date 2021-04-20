import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article Class.
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test.
        '''

        self.new_article = Article("David Murphy", "What You Need to Know About Buying Cryptocurrency on PayPal", "Whether you’re looking to make a larger investment or you just want to dabble in cryptocurrencies, you can purchase Bitcoin, Ethereum, Bitcoin Cash, and Litecoin through PayPal. And, soon, you’ll be able to pay various merchants using your cryptocurrency stas…",  "https://lifehacker.com/what-you-need-to-know-about-buying-cryptocurrency-on-pa-1846585705",  "https://i.kinja-img.com/gawker-media/image/upload/c_fill,f_auto,fl_progressive,g_center,h_675,pg_1,q_80,w_1200/qvc2foo4ufow1cbsuk9f.jpg", "2021-03-31T14:00:00Z")

    def test_instance(self):
        '''
        Test case to test if object instance is created.
        '''

        self.assertTrue(isinstance(self.new_article, Article))

    def test_init(self):
        '''
        Test case to test if object is initialised properly.
        '''

        self.assertEqual(self.new_article.author, "David Murphy")
        self.assertEqual(self.new_article.title, "What You Need to Know About Buying Cryptocurrency on PayPal")
        self.assertEqual(self.new_article.description, "Whether you’re looking to make a larger investment or you just want to dabble in cryptocurrencies, you can purchase Bitcoin, Ethereum, Bitcoin Cash, and Litecoin through PayPal. And, soon, you’ll be able to pay various merchants using your cryptocurrency stas…")
        self.assertEqual(self.new_article.url, "https://lifehacker.com/what-you-need-to-know-about-buying-cryptocurrency-on-pa-1846585705")
        self.assertEqual(self.new_article.urlToImage, "https://i.kinja-img.com/gawker-media/image/upload/c_fill,f_auto,fl_progressive,g_center,h_675,pg_1,q_80,w_1200/qvc2foo4ufow1cbsuk9f.jpg")
        self.assertEqual(self.new_article.publishedAt, "2021-03-31T14:00:00Z")