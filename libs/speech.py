from google.cloud import speech as sclient

class Speech:
    
    def request_transcription(self, payload):
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

