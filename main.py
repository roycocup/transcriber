from libs.bucket import Bucket
from google.cloud.speech import RecognitionAudio, RecognitionConfig, SpeechClient
import time

def test_connect():
    bucket = Bucket()
    buckets = bucket.get_all_buckets()
    all_files = bucket.get_all_files(buckets)
    print(all_files)

def proof_of_concept():
    config = RecognitionConfig(
        encoding=RecognitionConfig.AudioEncoding.FLAC,
        language_code="en-UK",
        audio_channel_count=2
    )
    audio = RecognitionAudio(uri='gs://general-rodderscode-co-uk/test.flac')
    response = SpeechClient().recognize(config=config, audio=audio)
    print(response)



