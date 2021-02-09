from google.cloud import speech as sclient


class Speech:

    def request_transcription(self, configuration, recognition_audio):
        '''
        * gets a RecognitionAudio or SpeechAsyncClient for google
        * makes configuration as payload to google
        * gets a sync or asyn response
        * stores ref to asyn or stores respose as json
        '''

        response = sclient.SpeechClient().recognize(
            config=configuration, audio=recognition_audio)

        return response
