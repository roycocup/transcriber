from tests.base import Base
from libs.speech import Speech
from google.cloud import speech as gspeech
from unittest.mock import MagicMock

class TestSpeech(Base):

    # def setUp(self):
    #     self.sut = Speech()
        
    # https://docs.python.org/3/library/unittest.mock-examples.html
    def test_request_transcription(self):
        mocked = gspeech.SpeechClient()
        mocked.recognize = MagicMock()
        mocked.recognize.assert_called_once_with({})
        sut = Speech(mocked)
        sut.request_transcription(1)
        # self.sut.request_transcription(configuration)
        