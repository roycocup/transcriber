from behave import *
from features.steps.utils import *
from libs import bucket
from libs import gfiles
from libs import speech
import os

sut = speech.Speech()
test_filename = 'test.mp3'
test_bucket_name = None

@given(u'we have a test file in "{bucket_name}"')
def step_impl(context, bucket_name):
    test_bucket_name = bucket_name
    create_test_bucket(test_bucket_name)
    gfile = gfiles.GFiles(test_bucket_name)
    gfile.upload(test_filename)


@when(u'we ask for a transcription')
def step_impl(context):
    pass


@then(u'we get a transcription json')
def step_impl(context):
    delete_test_bucket(test_bucket_name)