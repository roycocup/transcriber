from google.cloud import speech as sclient

class Speech:
    
    def request_transcription(self, configuration):
        '''
        * create the gs:// uri for the file based on payload
        * gets a RecognitionAudio or SpeechAsyncClient for google
        * makes configuration as payload to google
        * gets a sync or asyn response
        * stores ref to asyn or stores respose as json
        
        Payload to google should look like this
        {
            "config": {
                "encoding":"FLAC",
                "sampleRateHertz": 16000,
                "languageCode": "en-UK",
                "enableWordTimeOffsets": false
            },
            "audio": {
                "uri":"gs://cloud-samples-tests/speech/brooklyn.flac"
            }
        }
        '''
        
        # gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"
        # audio = speech.RecognitionAudio(uri=gcs_uri)
        # config = speech.RecognitionConfig(
        #     encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        #     sample_rate_hertz=16000,
        #     language_code="en-UK",
        # )
        # response = client.recognize(config=config, audio=audio)
        # for result in response.results:
        #     print("Transcript: {}".format(result.alternatives[0].transcript))
        return sclient.recognize({})

