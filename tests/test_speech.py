from tests.base import Base
from libs.speech import Speech
from unittest import mock
import json

class TestSpeech(Base):

    def setUp(self):
        self.sut = Speech()
        
    # https://docs.python.org/3/library/unittest.mock-examples.html
    @mock.patch('libs.speech.reconAudio')
    @mock.patch('libs.speech.sclient')
    def test_request_transcription_returns_json(self, mock_speech, mock_audio):
        mock_response_data = json.dumps({'this':'the response'})
        mock_speech.recognize.return_value = mock_response_data
        
        configuration = {
            "config": {
                "encoding":"FLAC",
                "sampleRateHertz": 16000,
                "languageCode": "en-UK",
                "enableWordTimeOffsets": False
            },
            "audio": {
                "uri":"gc://somebucket/somefile.mp3"
            }
        }

        # call to sut
        actual = self.sut.request_transcription(configuration)

        
        mock_audio.assert_called_once_with(uri="gc://somebucket/somefile.mp3")
        mock_speech.recognize.assert_called()
        
        self.assertEquals(actual, mock_response_data)

    # def test_get_audio_config(self):
    #     expected = 
    #     self.assertEquals(actual, mock_response_data)

    

    
    
    
        



        



        
        