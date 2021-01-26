from tests.base import Base
from libs.speech import Speech

class TestSpeech(Base):

    def setUp(self):
        self.sut = Speech()

    def test_instantiates(self):
        self.assertTrue(True)
        