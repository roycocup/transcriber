from tests.base import Base
from libs.speech import Speech
from unittest import mock
import json

class TestSpeech(Base):

    # def setUp(self):
    #     self.sut = Speech()
        
    # https://docs.python.org/3/library/unittest.mock-examples.html
    @mock.patch('libs.speech.sclient')
    def test_request_transcription_returns_json_from_client(self, mock_speech):
        sut = Speech()
        mock_response_data = json.dumps({'this':'the response'})
        mock_speech.recognize.return_value = mock_response_data
        
        actual = sut.request_transcription({})

        mock_speech.recognize.assert_called_with({})
        self.assertEquals(actual, mock_response_data)
    
    
        



        



        
        