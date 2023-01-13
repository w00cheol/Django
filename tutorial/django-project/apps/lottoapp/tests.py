from django.test import TestCase

# Create your tests here.
from .models import GuessNumbers

class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        g = GuessNumbers(name='woo', text='테스트케이스1')
        g.generate()
        print(g.update_date)
        print(g.lottos)
        self.assertTrue(len(g.lottos) >= g.num_lotto * 6)