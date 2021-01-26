from behave import *
from libs import bucket
from libs import gfiles
from libs import speech
from features.steps.utils import *
import os

sut = speech.Speech()
test_filename = 'test.mp3'

@given(u'we have a test file in "{bucket_name}"')
def step_impl(context, bucket_name):
    gfile = gfiles.GFiles(bucket_name)
    gfile.upload(test_filename)


@when(u'we ask for a transcription')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we ask for a transcription')


@then(u'we get a transcription json')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we get a transcription json')