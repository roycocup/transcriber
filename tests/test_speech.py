from tests.base import Base
from libs.speech import Speech
from unittest import mock
import json

class TestSpeech(Base):

    def setUp(self):
        self.sut = Speech()
        
    # https://docs.python.org/3/library/unittest.mock-examples.html
    
    @mock.patch('libs.speech.sclient')
    def test_request_transcription_returns_json(self, mock_speech):
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

        from google.cloud.speech import RecognitionAudio
        mock_recon_audio = mock.Mock(RecognitionAudio)

        # mock_speech.recognize.assert_called_with(configuration=configuration, audio=mock_recon_audio)
        # mock_recon_audio.assert_any_call()
        
        # call to sut
        actual = self.sut.request_transcription(configuration=configuration, recognition_audio=mock_recon_audio)

        
        
        self.assertEqual(actual, mock_response_data)

    
    

    
    
    
        



        



        
        