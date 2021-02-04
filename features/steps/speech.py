from behave import *
from features.steps.utils import *
from libs import bucket
from libs import gfiles
from libs import speech
from libs.uri_creator import UriCreator
import os
from google.cloud.speech import RecognitionAudio, RecognitionConfig

sut = speech.Speech()
test_filename = 'test.mp3'

test_config = {
    "config": {
        "encoding":"MP3",
        "sampleRateHertz": 16000,
        "languageCode": "en-UK",
        "enableWordTimeOffsets": "false"
    },
    "audio": {
        "uri": None
    }
}


@given(u'we have a test file in "{bucket_name}"')
def step_impl(context, bucket_name):
    context.bucket_name = bucket_name
    create_test_bucket(bucket_name)
    gfile = gfiles.GFiles(bucket_name)
    gfile.upload(test_filename)
    


@when(u'we ask for a transcription')
def step_impl(context):
    uri = UriCreator.get_uri(context.bucket_name, test_filename)
    print(uri)
    config = RecognitionConfig(
        encoding=RecognitionConfig.AudioEncoding.OGG_OPUS,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    audio = RecognitionAudio(uri=uri)
    context.ref = sut.request_transcription(configuration=config, recognition_audio=audio)


@then(u'we get a transcription json')
def step_impl(context):
    delete_test_bucket(context.bucket_name)
    if context.ref is None:
        raise Exception('Nothing came back from google speech')

    