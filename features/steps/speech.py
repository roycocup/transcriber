from behave import *
from features.steps.utils import *
from libs import bucket
from libs import gfiles
from libs import speech
from libs.uri_creator import UriCreator
import os
from google.cloud.speech import *

sut = speech.Speech()
test_filename = 'test.flac'


@given(u'we have a test file in "{bucket_name}"')
def step_impl(context, bucket_name):
    context.bucket_name = bucket_name
    create_test_bucket(bucket_name)
    gfile = gfiles.GFiles(bucket_name)
    gfile.upload(test_filename)
    


@when(u'we ask for a transcription')
def step_impl(context):
    uri = UriCreator.get_uri(context.bucket_name, test_filename)
    config = RecognitionConfig(
        encoding=RecognitionConfig.AudioEncoding.FLAC,
        language_code="en-UK",
        audio_channel_count=2
    )
    audio = RecognitionAudio(uri=uri)
    context.ref = sut.request_transcription(configuration=config, recognition_audio=audio)


@then(u'we get a transcription json')
def step_impl(context):
    delete_test_bucket(context.bucket_name)
    if context.ref is None:
        raise Exception('Nothing came back from google speech')


@when(u'we ask for a transcription asyncronously')
def step_impl(context):
    uri = UriCreator.get_uri(context.bucket_name, test_filename)
    config = RecognitionConfig(
        encoding=RecognitionConfig.AudioEncoding.FLAC,
        language_code="en-UK",
        audio_channel_count=2
    )
    audio = RecognitionAudio(uri=uri)
    context.token = sut.request_asyncronous_transcription(configuration=config, recognition_audio=audio)


@then(u'if we wait')
def step_impl(context):
    context.ref = context.token.result(timeout=90)


@then(u'we get a token')
def step_impl(context):
    assert context.token is not None
