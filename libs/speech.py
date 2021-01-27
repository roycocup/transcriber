
class Speech:
    def __init__(self, speech_client):
        self.speech_client = speech_client
    
    def request_transcription(self):
        self.speech_client.recognize(1)


# # Instantiates a client
# client = speech.SpeechClient()

# # The name of the audio file to transcribe
# gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"

# audio = speech.RecognitionAudio(uri=gcs_uri)

# config = speech.RecognitionConfig(
#     encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#     sample_rate_hertz=16000,
#     language_code="en-US",
# )

# # Detects speech in the audio file
# response = client.recognize(config=config, audio=audio)

# for result in response.results:
#     print("Transcript: {}".format(result.alternatives[0].transcript))